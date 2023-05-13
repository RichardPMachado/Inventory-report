from .inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.importer.csv_importer import CsvImporter
# from inventory_report.importer.json_importer import JsonImporter
# from inventory_report.importer.xml_importer import XmlImporter
# from collections.abc import Iterable


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = list()

    def import_data(self, path, report):
        # type_report = InventoryRefactor.verify_path(path)
        new_data = self.importer.import_data(path)
        # print("oi", dir(self.data))
        self.data.extend(new_data)
        # if type_report == ".csv":
        #     report_read = CsvImporter.import_data(path)
        # elif type_report == ".json":
        #     report_read = JsonImporter.import_data(path)
        # else:
        #     report_read = XmlImporter.import_data(path)

        if report == "simples":
            return SimpleReport.generate(new_data)

        return CompleteReport.generate(new_data)

    def __iter__(self):
        print("oi", self.data)
        return InventoryIterator(self.data)

    # @classmethod
    # def verify_path(cls, path):
    #     type_report = os.path.splitext(path)[1]
    #     return type_report
