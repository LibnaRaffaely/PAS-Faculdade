"""Contrato comum a todos os filtros do pipeline."""

from abc import ABC, abstractmethod
from typing import Any


class Filter(ABC):
    """Um filtro recebe uma entrada e produz uma saída.

    Nenhum filtro deve conhecer a implementação interna de outro:
    a comunicação acontece apenas através de process(entrada) -> saida.
    """

    @abstractmethod
    def process(self, entrada: Any) -> Any:
        raise NotImplementedError
