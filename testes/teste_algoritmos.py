from classes.alg_impl.BestFit import BestFit
from classes.alg_impl.FirstFit import FirstFit
from classes.alg_impl.WorstFit import WorstFit
from classes.Algoritmo import Algoritmo
from classes.Byte import Byte

# Função para inicializar a memória
def inicializa_memoria(tamanho_total: int) -> list:
    return [Byte() for _ in range(tamanho_total)]

# Teste de alocação
def testa_algoritmos():
    # Cenário 1: Espaço suficiente para alocação
    mem = inicializa_memoria(16)
    mem[5].id = 0
    mem[5].idx_ini = 5
    mem[5].tam = 1
    mem[12].id = 1
    mem[12].idx_ini = 12
    mem[12].tam = 1

    print("\nCenário 1: Alocação bem-sucedida")
    best_fit = BestFit()
    worst_fit = WorstFit()
    first_fit = FirstFit()

    print("BestFit:")
    print(best_fit.procura_bloco_livre(mem, 3, 2, True))
    print("WorstFit:")
    print(worst_fit.procura_bloco_livre(mem, 3, 3, True))
    print("FirstFit:")
    print(first_fit.procura_bloco_livre(mem, 3, 4, True))

    for elem in mem:
        print(f"id: {elem.id}; idx_ini: {elem.idx_ini}; tam: {elem.tam}")

    # Cenário 2: Falha de alocação (nenhum espaço contíguo de tamanho 3 ou maior)
    mem = inicializa_memoria(10)
    mem[1].id = 0; mem[1].idx_ini = 1; mem[1].tam = 1
    mem[3].id = 1; mem[3].idx_ini = 3; mem[3].tam = 1
    mem[5].id = 2; mem[5].idx_ini = 5; mem[5].tam = 1
    mem[7].id = 3; mem[7].idx_ini = 7; mem[7].tam = 1
    mem[9].id = 4; mem[9].idx_ini = 9; mem[9].tam = 1

    print("\nCenário 2: Falha na alocação")
    print("BestFit:")
    print(best_fit.procura_bloco_livre(mem, 3, 10, True))  # Tentando alocar um bloco de tamanho 3
    print("WorstFit:")
    print(worst_fit.procura_bloco_livre(mem, 3, 11, True))  # Tentando alocar um bloco de tamanho 3
    print("FirstFit:")
    print(first_fit.procura_bloco_livre(mem, 3, 12, True))  # Tentando alocar um bloco de tamanho 3

    for elem in mem:
        print(f"id: {elem.id}; idx_ini: {elem.idx_ini}; tam: {elem.tam}")

# Chama o teste
if __name__ == "__main__":
    testa_algoritmos()
