
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from filters.clean_filter import CleanFilter
from filters.transform_filter import TransformFilter
from filters.sum_filter import SumFilter
from filters.report_filter import ReportFilter
from filters.read_filter import ReadFilter
from models import RawSale, ValidSale, TransformedSale, SalesSummary


class TestCleanFilter(unittest.TestCase):
    def test_descarta_quantidade_menor_ou_igual_a_zero(self):
        entrada = [RawSale("1", "Mouse", "-1", "90.00")]
        resultado = CleanFilter().process(entrada)
        self.assertEqual(resultado, [])

    def test_descarta_preco_ausente(self):
        entrada = [RawSale("1", "Mouse", "2", "")]
        resultado = CleanFilter().process(entrada)
        self.assertEqual(resultado, [])

    def test_descarta_dados_numericos_invalidos(self):
        entrada = [RawSale("1", "Mouse", "abc", "90.00")]
        resultado = CleanFilter().process(entrada)
        self.assertEqual(resultado, [])

    def test_mantem_registro_valido(self):
        entrada = [RawSale("1", "Mouse", "5", "90.00")]
        resultado = CleanFilter().process(entrada)
        self.assertEqual(resultado, [ValidSale("1", "Mouse", 5, 90.00)])


class TestTransformFilter(unittest.TestCase):
    def test_calcula_valor_total(self):
        entrada = [ValidSale("1", "Mouse", 5, 90.00)]
        resultado = TransformFilter().process(entrada)
        self.assertEqual(resultado, [TransformedSale("1", "Mouse", 5, 90.00, 450.00)])


class TestSumFilter(unittest.TestCase):
    def test_agrega_vendas(self):
        entrada = [
            TransformedSale("1", "Mouse", 5, 90.00, 450.00),
            TransformedSale("2", "Monitor", 1, 1200.00, 1200.00),
        ]
        resultado = SumFilter().process(entrada)
        self.assertEqual(resultado, SalesSummary(vendas_validas=2, produtos_vendidos=6, valor_total=1650.00))

    def test_lista_vazia(self):
        resultado = SumFilter().process([])
        self.assertEqual(resultado, SalesSummary(vendas_validas=0, produtos_vendidos=0, valor_total=0))


class TestReportFilter(unittest.TestCase):
    def test_relatorio_contem_os_dados_principais(self):
        entrada = SalesSummary(vendas_validas=8, produtos_vendidos=20, valor_total=14630.00)
        relatorio = ReportFilter().process(entrada)
        self.assertIn("Vendas válidas:   8", relatorio)
        self.assertIn("Produtos vendidos: 20", relatorio)
        self.assertIn("14.630,00", relatorio)


class TestReadFilter(unittest.TestCase):
    def test_le_arquivo_de_10_registros(self):
        caminho = os.path.join(os.path.dirname(__file__), "..", "..", "vendas_exemplo_10_linhas.csv")
        registros = ReadFilter(caminho).process()
        self.assertEqual(len(registros), 10)
        self.assertEqual(registros[0], RawSale("001", "Notebook", "2", "4500.00"))


class TestPipelineCompleto(unittest.TestCase):
    def test_resultado_esperado_para_arquivo_de_10_registros(self):
        caminho = os.path.join(os.path.dirname(__file__), "..", "..", "vendas_exemplo_10_linhas.csv")

        brutos = ReadFilter(caminho).process()
        validos = CleanFilter().process(brutos)
        transformados = TransformFilter().process(validos)
        resumo = SumFilter().process(transformados)

        self.assertEqual(resumo, SalesSummary(vendas_validas=8, produtos_vendidos=20, valor_total=14630.00))


if __name__ == "__main__":
    unittest.main()
