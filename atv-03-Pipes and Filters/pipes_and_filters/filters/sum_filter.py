"""Filtro 4: agregação.

Entrada:  list[TransformedSale]
Saída:    SalesSummary
"""

from typing import List

from filters.base import Filter
from models import TransformedSale, SalesSummary


class SumFilter(Filter):
    def process(self, entrada: List[TransformedSale]) -> SalesSummary:
        return SalesSummary(
            vendas_validas=len(entrada),
            produtos_vendidos=sum(venda.quantidade for venda in entrada),
            valor_total=sum(venda.valor_total for venda in entrada),
        )
