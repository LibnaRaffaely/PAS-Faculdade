
from dataclasses import dataclass


@dataclass
class RawSale:
    """Registro bruto, exatamente como veio do CSV (tudo em string)."""
    id_venda: str
    produto: str
    quantidade: str
    preco_unitario: str


@dataclass
class ValidSale:
    """Registro já validado e convertido para os tipos corretos."""
    id_venda: str
    produto: str
    quantidade: int
    preco_unitario: float


@dataclass
class TransformedSale:
    """Registro válido acrescido do valor total calculado."""
    id_venda: str
    produto: str
    quantidade: int
    preco_unitario: float
    valor_total: float


@dataclass
class SalesSummary:
    """Resultado agregado de todas as vendas válidas."""
    vendas_validas: int
    produtos_vendidos: int
    valor_total: float
