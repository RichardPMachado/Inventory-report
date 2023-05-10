import pandas as pd
from .importer import Importer


class CsvImporter(Importer):
    def __init__(self) -> None:
        pass

    @classmethod
    def import_data(cls, path):
        if not path.endswith('.csv'):
            raise ValueError("Arquivo inválido")
        csv_read = pd.read_csv(path)
        dict_list = csv_read.to_dict('records')
        # refatoramento para tranformar o id para string
        a = list()
        for e in dict_list:
            e["id"] = str(e["id"])
            a.append(e)
        return a
