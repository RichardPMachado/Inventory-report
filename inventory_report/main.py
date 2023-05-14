import sys
import os
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    try:
        path, type = sys.argv[1:]
        report_type = os.path.splitext(path)[1]
        test = report_type[1:]
        # expression = eval(f"{test}Importer")
        # print(test)
        csvImporter = CsvImporter
        xmlImporter = XmlImporter
        jsonImporter = JsonImporter
        print("oi", csvImporter, jsonImporter, xmlImporter)

        report = InventoryRefactor(
            eval(f"{test}Importer")).import_data(path, type)

        sys.stdout.write(report)

    except (IndexError, KeyError, ValueError):
        sys.stderr.write("Verifique os argumentos\n")
