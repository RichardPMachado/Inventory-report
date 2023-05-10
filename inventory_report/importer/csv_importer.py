import pandas as pd
from .importer import Importer


class CsvImporter(Importer):

    @classmethod
    def import_data(cls, path):
        if not path.endswith('.csv'):
            raise ValueError("Arquivo inválido")
        csv_read = pd.read_csv(path)
        dict_list = csv_read.to_dict('records')
        return dict_list
