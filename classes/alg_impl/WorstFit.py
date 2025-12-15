from classes.Algoritmo import Algoritmo
from classes.Byte import Byte


class WorstFit(Algoritmo):
    s WorstFit(Algoritmo):
        """
            Implementação do algoritmo Worst Fit para alocação dinâmica de memória.

            A estratégia consiste em percorrer toda a memória simulada em busca do
            maior bloco livre disponível e utilizá-lo para a alocação, buscando
            minimizar a criação de pequenos fragmentos livres.
        """

    def procura_bloco_livre(self, mem: list[Byte], tam_bloco: int, id: int) -> int:
         """
            Procura o maior bloco livre disponível e realiza a alocação caso o
            espaço seja suficiente para o tamanho solicitado.

            :param mem: Lista que representa a memória física simulada.
            :param tam_bloco: Tamanho do bloco a ser alocado.
            :param id: Identificador único do bloco alocado.
            :return: Índice inicial do bloco alocado ou -1 caso não exista espaço.
         """
        i = 0
        max_idx_ini = -1
        max_tam_possivel = -1
        while i < len(mem):
            if mem[i].idx_ini > -1:
                i += mem[i].tam
            else:
                idx_ini = i
                tam_possivel = 1
                while idx_ini + tam_possivel < len(mem) and mem[idx_ini + tam_possivel].id == -1:
                    tam_possivel += 1
                if tam_possivel > max_tam_possivel:
                    max_idx_ini = idx_ini
                    max_tam_possivel = tam_possivel
                i += tam_possivel
        if max_tam_possivel >= tam_bloco:
            for i in range(max_idx_ini, max_idx_ini + tam_bloco):
                mem[i].id = id
                mem[i].idx_ini = max_idx_ini
                mem[i].tam = tam_bloco
            return max_idx_ini
        return -1