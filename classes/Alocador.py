from classes.Algoritmo import Algoritmo


class Alocador:

    # Possível transformar em um método comum
    def __init__(self, tamanho=64):
        self.tam_mem = tamanho
        self.memoria = []
        self.prox_id = 0
        for _ in range(self.tamanho):
            self.memoria.append(-1)

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
