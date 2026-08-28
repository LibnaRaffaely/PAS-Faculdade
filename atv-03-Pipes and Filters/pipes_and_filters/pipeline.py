
from typing import Any, List

from filters.base import Filter


class Pipeline:
    def __init__(self, filtros: List[Filter]):
        self._filtros = filtros

    def run(self, entrada_inicial: Any = None) -> Any:
        dado = entrada_inicial
        for filtro in self._filtros:
            dado = filtro.process(dado)
        return dado
