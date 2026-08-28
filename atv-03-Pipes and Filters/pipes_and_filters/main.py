"""Ponto de entrada da aplicação.

Uso:
    python main.py caminho/para/arquivo.csv
    python main.py                      (usa o arquivo de 10 registros por padrão)
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from filters.read_filter import ReadFilter
from filters.clean_filter import CleanFilter
from filters.transform_filter import TransformFilter
from filters.sum_filter import SumFilter
from filters.report_filter import ReportFilter
from pipeline import Pipeline

ARQUIVO_PADRAO = "../vendas_exemplo_10_linhas.csv"


def main():
    caminho_arquivo = sys.argv[1] if len(sys.argv) > 1 else ARQUIVO_PADRAO

    clean_filter = CleanFilter()

    pipeline = Pipeline([
        ReadFilter(caminho_arquivo),
        clean_filter,
        TransformFilter(),
        SumFilter(),
        ReportFilter(),
    ])

    relatorio = pipeline.run()
    print(relatorio)

    if clean_filter.descartados:
        print(f"\n{len(clean_filter.descartados)} registro(s) descartado(s) na validação:")
        for registro, motivo in clean_filter.descartados:
            print(f"  - id_venda={registro.id_venda!r}: {motivo}")


if __name__ == "__main__":
    main()
