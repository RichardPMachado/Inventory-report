import os
import pandas as pd
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def import_data(cls, path, report):
        type_report = cls.verify_path(path)

        if type_report == ".csv":
            report_read = cls.csv_report(path)
        elif type_report == ".json":
            report_read = cls.json_report(path)
        else:
            report_read = cls.xml_report(path)

        if report == "simples":
            return SimpleReport.generate(report_read)

        return CompleteReport.generate(report_read)

    @classmethod
    def csv_report(cls, path):
        csv_read = pd.read_csv(path)
        dict_list = csv_read.to_dict('records')
        return dict_list

    @classmethod
    def json_report(cls, path):
        json_read = pd.read_json(path)
        dict_list = json_read.to_dict('records')
        return dict_list

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
        type_report = os.path.splitext(path)[1]
        return type_report
