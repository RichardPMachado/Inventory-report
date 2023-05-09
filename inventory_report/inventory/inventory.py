import os
import pandas as pd
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xml.etree.ElementTree as ET


class Inventory:
    @staticmethod
    def import_data(path: str, report: str):
        type_report = Inventory.verify_path(path)
        print('ooooo', type_report)

        if (type_report == ".csv"):
            report_read = Inventory.csv_report(path),
        elif (type_report == ".json"):
            report_read = Inventory.json_report(path),
        else:
            report_read = Inventory.xml_report(path)

        # print(report_read)
        if (report == "completo"):
            complet_simple_report = CompleteReport.generate(report_read)
        else:
            complet_simple_report = SimpleReport.generate(report_read)
        return complet_simple_report

    @classmethod
    def csv_report(cls, path):
        csv_read = pd.read_csv(path)
        lista_de_dict = csv_read.to_dict('records')
        return lista_de_dict

    @classmethod
    def json_report(cls, path):
        json_read = pd.read_json(path)
        lista_de_dict = json_read.to_dict('records')
        return lista_de_dict

    @classmethod
    def xml_report(cls, path):
        tree = ET.parse(path)
        root = tree.getroot()
        data = []

        for element in root:
            prod = {}
            for child in element:
                prod[child.tag] = child.text
            data.append(prod)
        return data

    @classmethod
    def verify_path(cls, path):
        type_report = os.path.splitext(path)
        return type_report
