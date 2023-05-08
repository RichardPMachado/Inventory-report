from typing import List, Dict
import datetime


class SimpleReport:
    @staticmethod
    def generate(prod: List[Dict]) -> str:
        current_date = datetime.date.today()

        Oldest = min(prod, key=lambda p: p['data_de_fabricacao'])
        exp_date = min(
            prod, key=lambda p: abs(datetime
                                    .datetime
                                    .strptime(p[
                                        'data_de_validade'], '%Y-%m-%d')
                                    .date() - current_date))

        empresas = dict()
        for produto in prod:
            if produto["nome_da_empresa"] in empresas:
                empresas[produto["nome_da_empresa"]] += 1
            else:
                empresas[produto["nome_da_empresa"]] = 1

        empresa_com_mais_produtos = max(empresas, key=empresas.get)

    # print(
    #     f"Data de fabricação mais antiga: {Oldest['data_de_fabricacao']}\n"
    #     f"Data de validade mais próxima: {exp_date['data_de_validade']}\n"
    #     f"Empresa com mais produtos: {empresa_com_mais_produtos}")
        return (
            f"Data de fabricação mais antiga: {Oldest['data_de_fabricacao']}\n"
            f"Data de validade mais próxima: {exp_date['data_de_validade']}\n"
            f"Empresa com mais produtos: {empresa_com_mais_produtos}")
