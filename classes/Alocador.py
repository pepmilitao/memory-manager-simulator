from classes.Algoritmo import Algoritmo
from classes.Byte import Byte


class Alocador:
    """
        Classe responsável por gerenciar a memória simulada.
        Centraliza as operações de inicialização, alocação e liberação.
    """

    def __init__(self):
        self.inicializado = False

    def init(self, tamanho: int) -> None:
        """
            Inicializa a memória física simulada com o tamanho informado.
            Todos os bytes são marcados inicialmente como livres.
        """
        if tamanho <= 0:
            raise ValueError("O tamanho da memória deve ser diferente de 0.")
        self.tam_mem = tamanho
        self.memoria = [Byte() for _ in range(tamanho)]
        self.prox_id = 1
        self.inicializado = True

    # Aloca bloco na memória
    def alloc(self, tamanho: int, alg: Algoritmo) -> bool:
        ret = alg.procura_bloco_livre(self.memoria, tamanho, self.prox_id, True)
        self.prox_id += 1
        if ret == -1:
            return False
        return True

    # Libera bloco com base em um id
    def free_id(self, id: int) -> bool:
        i = 0
        while i < len(self.memoria):
            if self.memoria[i].id == id:
                for j in range(i, i + self.memoria[i].tam):
                    self.memoria[i].reset()
                return True
            i += 1
        return False
                    

    # Escolhe o bloco ideal sem alocar ele
    def choose_block(self, tamanho: int, alg: Algoritmo) -> dict:
        idx = alg.procura_bloco_livre(self.memoria, tamanho, self.prox_id, False)
        ret = {
            "id": self.prox_id,
            "idx_ini": idx,
            "tam": tamanho
        }
        return ret

    # Exibe estado atual do bloco em duas linhas: uso físico e id's
    def show(self) -> None:
        print("TODO")

    # Calcula e exibe métricas de uso
    def stats(self) -> None:
        print("TODO")
