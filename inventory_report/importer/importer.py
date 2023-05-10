from abc import ABC, abstractmethod


class Importer(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def import_data(cls):
        raise NotImplementedError
