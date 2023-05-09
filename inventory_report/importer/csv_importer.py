from .importer import Importer
from pandas import pd


class CsvImporter(Importer):
    def __init__(self) -> None:
        pass

    @staticmethod
    def import_data(cls, path):
        try:
            if not path.endswith('.csv'):
                raise ValueError("Arquivo inválido")
            csv_read = pd.read_csv(path)
            dict_list = csv_read.to_dict('records')
            return dict_list
        except ValueError:
            raise ValueError
