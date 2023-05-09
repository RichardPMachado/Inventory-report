import os
from pandas import pd
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
            json_read = pd.read_json(path)
            dict_list = json_read.to_dict('records')
            return dict_list
        except ValueError:
            raise ValueError
