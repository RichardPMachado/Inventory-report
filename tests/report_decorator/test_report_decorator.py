from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

FINISH_DECO = "\033[0m"
BLUE_DECO = "\033[36m"
GREEN_DECOR = "\033[32m"
RED_DECO = "\033[31m"

mock_prod = [{
    "id": 1,
    "nome_do_produto": "Nicotine Polacrilex",
    "nome_da_empresa": "Target Corporation",
    "data_de_fabricacao": "2021-02-18",
    "data_de_validade": "2023-09-17",
    "numero_de_serie": "CR25 1551 4467 2549 4402 1",
    "instrucoes_de_armazenamento": "instrucao 1",
}]


FABRICATION_DATE = mock_prod[0]["data_de_fabricacao"]
EXPIRATION_DATE = mock_prod[0]["data_de_validade"]
COMPANY_NAME = mock_prod[0]["nome_da_empresa"]
fabr_oldest = f"{GREEN_DECOR}Data de fabricação mais antiga:{FINISH_DECO}"
Nearest_exp_date = f"{GREEN_DECOR}Data de validade mais próxima:{FINISH_DECO}"
more_products = f"{GREEN_DECOR}Empresa com mais produtos:{FINISH_DECO}"
prod_report = "Produtos estocados por empresa:"

expected_simple_report = (
    f"{fabr_oldest} {BLUE_DECO}{FABRICATION_DATE}{FINISH_DECO}\n"
    f"{Nearest_exp_date} {BLUE_DECO}{EXPIRATION_DATE}{FINISH_DECO}\n"
    f"{more_products} {RED_DECO}{COMPANY_NAME}{FINISH_DECO}"
)
expected_complete_report = (
    f"{expected_simple_report}\n"
    f"{prod_report}\n"
    "- Target Corporation: 1\n"
)


def test_decorar_relatorio():
    color_complete_report = ColoredReport(CompleteReport).generate(mock_prod)
    color_simple_report = ColoredReport(SimpleReport).generate(mock_prod)
    # print(color_complete_report)
    print(expected_complete_report)
    # print(color_simple_report)
    assert color_simple_report == expected_simple_report
    assert color_complete_report == expected_complete_report
