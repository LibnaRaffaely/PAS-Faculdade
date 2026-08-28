"""Filtro 5: geração do relatório.

Entrada:  SalesSummary
Saída:    str (relatório formatado)
"""

from filters.base import Filter
from models import SalesSummary

LARGURA = 40


class ReportFilter(Filter):
    def process(self, entrada: SalesSummary) -> str:
        separador = "=" * LARGURA
        valor_formatado = f"R$ {entrada.valor_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        linhas = [
            separador,
            "RELATÓRIO DE VENDAS".center(LARGURA),
            separador,
            "",
            f"Vendas válidas:   {entrada.vendas_validas}",
            f"Produtos vendidos: {entrada.produtos_vendidos}",
            f"Valor total:      {valor_formatado}",
            "",
            separador,
        ]
        return "\n".join(linhas)
