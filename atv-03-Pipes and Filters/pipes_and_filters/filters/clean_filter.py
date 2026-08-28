"""Filtro 2: limpeza e validação.

Entrada:  list[RawSale]
Saída:    list[ValidSale]

Um registro é considerado inválido quando:
    - quantidade não é um número inteiro válido;
    - quantidade é menor ou igual a zero;
    - preco_unitario está ausente (vazio);
    - preco_unitario não é um número válido.

Registros inválidos são descartados e registrados em self.descartados,
para que o motivo do descarte fique documentado e possa ser inspecionado.
"""

from typing import List

from filters.base import Filter
from models import RawSale, ValidSale


class CleanFilter(Filter):
    def __init__(self):
        self.descartados: List[tuple] = []  # (RawSale, motivo)

    def process(self, entrada: List[RawSale]) -> List[ValidSale]:
        self.descartados = []
        validos = []

        for registro in entrada:
            motivo = self._motivo_invalidez(registro)
            if motivo:
                self.descartados.append((registro, motivo))
                continue

            validos.append(
                ValidSale(
                    id_venda=registro.id_venda,
                    produto=registro.produto,
                    quantidade=int(registro.quantidade),
                    preco_unitario=float(registro.preco_unitario),
                )
            )

        return validos

    @staticmethod
    def _motivo_invalidez(registro: RawSale) -> str:
        if not registro.preco_unitario:
            return "preco_unitario ausente"

        try:
            quantidade = int(registro.quantidade)
        except (TypeError, ValueError):
            return "quantidade não é um número inteiro válido"

        try:
            preco = float(registro.preco_unitario)
        except (TypeError, ValueError):
            return "preco_unitario não é um número válido"

        if quantidade <= 0:
            return "quantidade menor ou igual a zero"

        if preco < 0:
            return "preco_unitario negativo"

        return ""
