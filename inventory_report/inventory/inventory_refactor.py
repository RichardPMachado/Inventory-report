import os
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class InventoryRefactor:
    @classmethod
    def import_data(cls, path, report):
        type_report = cls.verify_path(path)

        if type_report == ".csv":
            report_read = CsvImporter.import_data(path)
        elif type_report == ".json":
            report_read = JsonImporter.import_data(path)
        else:
            report_read = XmlImporter.import_data(path)

        if report == "simples":
            return SimpleReport.generate(report_read)

        return CompleteReport.generate(report_read)

    @classmethod
    def verify_path(cls, path):
        type_report = os.path.splitext(path)[1]
        return type_report
