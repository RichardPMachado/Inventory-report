import os
from .importer import Importer


class JsonImporter(Importer):
    def __init__(self) -> None:
        pass

    @classmethod
    def import_data(cls, path):
        try:
            type_report = os.path.splitext(path)[1]
            if not type_report.endswith('.json'):
                raise ValueError("Arquivo inválido")
        except ValueError:
            raise ValueError
