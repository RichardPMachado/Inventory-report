from typing import List, Dict
from .simple_report import SimpleReport
# import datetime


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(prods: List[Dict]) -> str:
        simple_report_result = SimpleReport.generate(prods)
        companies = dict()
        for produto in prods:
            if produto["nome_da_empresa"] in companies:
                companies[produto["nome_da_empresa"]] += 1
            else:
                companies[produto["nome_da_empresa"]] = 1

        companies_list = list(companies.items())

        str_products_stock = ''

        for e in companies_list:
            str_products_stock += f"- {e[0]}: {e[1]}\n"

        # print(f"{str_products_stock}")

        return (
            f"{simple_report_result}\n"
            f"Produtos estocados por empresa:\n"
            f"{str_products_stock}"
            )
