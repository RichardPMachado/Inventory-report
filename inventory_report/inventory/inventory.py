import pandas as pd
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path: str, report: str):
        csv_read = Inventory.csv_report(path)
        if (report == "completo"):
            complet_simple_report = CompleteReport.generate(csv_read)
        else:
            complet_simple_report = SimpleReport.generate(csv_read)
        return complet_simple_report

    @classmethod
    def csv_report(cls, path):
        csv_read = pd.read_csv(path)
        lista_de_dict = csv_read.to_dict('records')
        return lista_de_dict
