"""Filtro 3: transformação.

Entrada:  list[ValidSale]
Saída:    list[TransformedSale]

Para cada venda válida calcula: valor_total = quantidade * preco_unitario
"""

from typing import List

from filters.base import Filter
from models import ValidSale, TransformedSale


class TransformFilter(Filter):
    def process(self, entrada: List[ValidSale]) -> List[TransformedSale]:
        return [
            TransformedSale(
                id_venda=venda.id_venda,
                produto=venda.produto,
                quantidade=venda.quantidade,
                preco_unitario=venda.preco_unitario,
                valor_total=venda.quantidade * venda.preco_unitario,
            )
            for venda in entrada
        ]
