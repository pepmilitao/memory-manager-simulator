from classes.Algoritmo import Algoritmo
from classes.Byte import Byte


class FirstFit(Algoritmo):
    """
        Implementação do algoritmo First Fit para alocação dinâmica de memória.

        A estratégia consiste em percorrer a memória e alocar o bloco no primeiro
        espaço livre contíguo que seja suficientemente grande para atender à
        requisição.
    """

    def procura_bloco_livre(self, mem: list[Byte], tam_bloco: int, id: int) -> int:
        """
            Procura o primeiro bloco livre e realiza a alocação imediatamente após encontrá-lo.

            :param mem: Lista que representa a memória física simulada.
            :param tam_bloco: Tamanho do bloco a ser alocado.
            :param id: Identificador único do bloco alocado.
            :return: Índice inicial do bloco alocado ou -1 caso não exista espaço.
        """
        i = 0
        # Percorre a memória até encontrar um bloco livre contíguo viável
        while i < len(mem):
            if mem[i].idx_ini > -1:
                i += mem[i].tam
            else:
                # Identifica o tamanho do bloco livre a partir da posição atual
                idx_ini = i
                tam_possivel = 1
                while idx_ini + tam_possivel < len(mem) and mem[idx_ini + tam_possivel].id == -1:
                    tam_possivel += 1
                    if tam_possivel >= tam_bloco:
                        for i in range(idx_ini, idx_ini + tam_bloco):
                            mem[i].id = id
                            mem[i].idx_ini = idx_ini
                            mem[i].tam = tam_bloco
                        return idx_ini
                i += tam_possivel
        return -1