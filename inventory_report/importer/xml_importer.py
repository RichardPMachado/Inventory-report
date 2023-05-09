from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def __init__(self) -> None:
        pass

    def import_data(cls, path):
        if not path.endswith('.xml'):
            raise ValueError("Arquivo inválido")
        tree = ET.parse(path)
        root = tree.getroot()
        data = []

        for element in root:
            prod = {}
            for child in element:
                prod[child.tag] = child.text
                data.append(prod)
        return data
