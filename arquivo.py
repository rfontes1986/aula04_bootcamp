import csv
from pathlib import Path

caminho_do_arquivo: str = "exemplo.csv"

arquivo_csv: list = []

# Tenta abrir o arquivo conforme informado (CWD). Se não existir, usa o
# caminho relativo ao arquivo do script (útil quando executado de outro CWD).
path = Path(caminho_do_arquivo)
if not path.exists():
    path = Path(__file__).parent / caminho_do_arquivo

with path.open(mode="r", encoding="utf_8") as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        # Remove espaços extras em chaves e valores
        arquivo_csv.append({k.strip(): v.strip() for k, v in linha.items()})

print(arquivo_csv)