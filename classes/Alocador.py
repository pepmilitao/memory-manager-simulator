from classes.Algoritmo import Algoritmo


class Alocador:
    """
        Classe responsável por gerenciar a memória simulada.
        Centraliza as operações de inicialização, alocação e liberação.
    """

    def __init__(self):
        self.tam_mem = tamanho
        self.memoria = list[Byte] = []
        self.prox_id = 1
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
    def alloc(self, tamanho: int, alg: Algoritmo) -> None:
        print("TODO")

    # Libera bloco com base em um id
    def free_id(self, id: int) -> None:
        print("TODO")

    # Escolhe o bloco ideal sem alocar ele
    def choose_block(self, tamanho: int, alg: Algoritmo) -> None:
        print("TODO")

    # Exibe estado atual do bloco em duas linhas: uso físico e id's
    def show(self) -> None:
        print("TODO")

    # Calcula e exibe métricas de uso
    def stats(self) -> None:
        print("TODO")
