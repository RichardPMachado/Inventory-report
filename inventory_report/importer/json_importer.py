import os
import pandas as pd
from .importer import Importer


class JsonImporter(Importer):
    def __init__(self) -> None:
        pass

    @classmethod
    def import_data(cls, path):
        type_report = os.path.splitext(path)[1]
        if not type_report.endswith('.json'):
            raise ValueError("Arquivo inválido")
        json_read = pd.read_json(path)
        dict_list = json_read.to_dict('records')
        # refatoramento para tranformar o id para string
        a = list()
        for e in dict_list:
            e["id"] = str(e["id"])
            a.append(e)
        # print(a)
        return dict_list
