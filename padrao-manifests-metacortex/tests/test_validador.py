"""Testes do validador do padrão da casa (camada de gate).

Regra do repo: validador sem teste negativo não é gate.
"""
import subprocess, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SCRIPT = RAIZ / "scripts" / "validar_padrao.py"
BARRADO = RAIZ / "tests" / "manifesto-barrado.yaml"


def rodar(alvo):
    r = subprocess.run([sys.executable, str(SCRIPT), str(alvo)],
                       capture_output=True, text=True)
    return r.returncode, r.stdout


def test_manifesto_barrado_falha():
    """O manifesto barrado da Seraph DEVE ser reprovado (exit 1)."""
    rc, out = rodar(BARRADO)
    assert rc == 1, f"esperado exit 1, veio {rc}"
    assert "FALHA" in out
    assert "3.3" in out, "segredo em texto puro deve ser apontado (regra 3.3)"
    assert "1.4" in out, "seletor cruzado deve ser apontado (regra 1.4)"


def test_manifesto_barrado_conta_falhas():
    rc, out = rodar(BARRADO)
    linha = [l for l in out.splitlines() if "falha(s)" in l]
    assert linha, "resumo de falhas ausente"
    n = int(linha[0].split("·")[1].strip().split()[0])
    assert n >= 15, f"esperado >=15 falhas no barrado, veio {n}"


if __name__ == "__main__":
    test_manifesto_barrado_falha()
    test_manifesto_barrado_conta_falhas()
    print("TESTES OK")
