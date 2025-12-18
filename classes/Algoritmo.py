from abc import ABC, abstractmethod
from classes.Byte import Byte


class Algoritmo(ABC):

    @abstractmethod
    def procura_bloco_livre(self, mem: list[Byte], tam_bloco: int, id: int, alocar: bool) -> int:
        pass