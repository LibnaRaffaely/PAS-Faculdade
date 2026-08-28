"""Filtro 1: leitura do arquivo CSV.

Entrada:  caminho do arquivo CSV (definido na construção do filtro)
Saída:    list[RawSale]
"""

import csv
from typing import List

from filters.base import Filter
from models import RawSale


class ReadFilter(Filter):
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo

    def process(self, entrada=None) -> List[RawSale]:
        registros = []
        with open(self.caminho_arquivo, newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                registros.append(
                    RawSale(
                        id_venda=(linha.get("id_venda") or "").strip(),
                        produto=(linha.get("produto") or "").strip(),
                        quantidade=(linha.get("quantidade") or "").strip(),
                        preco_unitario=(linha.get("preco_unitario") or "").strip(),
                    )
                )
        return registros
