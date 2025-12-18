from classes.alg_impl.BestFit import BestFit
from classes.alg_impl.FirstFit import FirstFit
from classes.alg_impl.WorstFit import WorstFit
from classes.Algoritmo import Algoritmo
from classes.Byte import Byte

def inicializa_memoria(tamanho_total: int) -> list:
    """
    Inicializa a memória como uma lista de objetos Byte com o tamanho especificado.
    """
    return [Byte() for _ in range(tamanho_total)]

def _imprime_memoria(mem: list):
    """
    Exibe o estado da memória: id, idx_ini e tam de cada Byte.
    """
    print("- Estado da memoria -")
    for i, elem in enumerate(mem):
        print(f"Pos {i}: id={elem.id}, idx_ini={elem.idx_ini}, tam={elem.tam}")
    print("-" * 30)

def teste01_alocacao_sucesso():
    """
    Testa alocação com espaço suficiente na memória.
    """
    print("\n[Cenário 1] Alocação bem-sucedida")
    mem = inicializa_memoria(16)
    # Marcando algumas posições como ocupadas manualmente (simulando outros blocos já alocados)
    mem[5].id = 0
    mem[5].idx_ini = 5
    mem[5].tam = 1
    mem[12].id = 1
    mem[12].idx_ini = 12
    mem[12].tam = 1

    best_fit = BestFit()
    worst_fit = WorstFit()
    first_fit = FirstFit()

    print("BestFit:", best_fit.procura_bloco_livre(mem, 3, 2, True))
    print("WorstFit:", worst_fit.procura_bloco_livre(mem, 3, 3, True))
    print("FirstFit:", first_fit.procura_bloco_livre(mem, 3, 4, True))

    _imprime_memoria(mem)

def teste02_alocacao_falha():
    """
    Testa tentativa de alocação sem espaço contíguo suficiente.
    """
    print("\n[Cenário 2] Falha na alocação")
    mem = inicializa_memoria(10)
    # Ocupando posições alternadas, sem espaço livre contíguo de 3 ou mais
    for pos, bloco_id in zip([1,3,5,7,9], range(5)):
        mem[pos].id = bloco_id
        mem[pos].idx_ini = pos
        mem[pos].tam = 1

    best_fit = BestFit()
    worst_fit = WorstFit()
    first_fit = FirstFit()

    print("BestFit:", best_fit.procura_bloco_livre(mem, 3, 10, True))
    print("WorstFit:", worst_fit.procura_bloco_livre(mem, 3, 11, True))
    print("FirstFit:", first_fit.procura_bloco_livre(mem, 3, 12, True))

    _imprime_memoria(mem)


def teste03_alocacao_apos_liberacao():
    """
    Testa se é possível reutilizar espaço após a liberação de um bloco.
    """
    print("\n[Cenário 3] Alocação após liberação")

    mem = inicializa_memoria(10)
    # Aloca um bloco de tamanho 4 usando FirstFit
    first_fit = FirstFit()
    idx = first_fit.procura_bloco_livre(mem, 4, 1, True)
    print(f"FirstFit (alocando 4): Índice alocado = {idx}")
    _imprime_memoria(mem)

    # Libera o bloco (simula a liberação)
    for i in range(idx, idx+4):
        mem[i].reset()
    print("Bloco liberado.")

    _imprime_memoria(mem)
    # Aloca novamente no mesmo espaço
    idx2 = first_fit.procura_bloco_livre(mem, 4, 2, True)
    print(f"FirstFit (realocando 4): Índice alocado = {idx2}")
    _imprime_memoria(mem)

def teste04_liberacao_invalida():
    """
    Testa tentativa de liberar um bloco inexistente.
    """
    print("\n[Cenário 4] Liberação de bloco inexistente")

    mem = inicializa_memoria(5)
    # Liberação de id que nunca foi alocado na memória "manual"
    resultado = False

    for elem in mem:
        if elem.id == 42:  # id fora do padrão dos testes
            elem.reset()
            resultado = True
    print("Resultado da liberação de bloco inexistente:", resultado)
    _imprime_memoria(mem)

def testa_algoritmos():
    """
    Executa diferentes cenários de teste para os algoritmos de alocação.
    """
    teste01_alocacao_sucesso()
    teste02_alocacao_falha()
    teste03_alocacao_apos_liberacao()
    teste04_liberacao_invalida()

if __name__ == "__main__":
    testa_algoritmos()
