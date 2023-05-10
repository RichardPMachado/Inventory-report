import os
import pandas as pd
from .importer import Importer


class JsonImporter(Importer):

    @classmethod
    def import_data(cls, path):
        type_report = os.path.splitext(path)[1]
        if not type_report.endswith('.json'):
            raise ValueError("Arquivo inválido")
        json_read = pd.read_json(path)
        dict_list = json_read.to_dict('records')
        return dict_list
