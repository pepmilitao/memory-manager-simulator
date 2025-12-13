from classes.Algoritmo import Algoritmo
from classes.Byte import Byte


class BestFit(Algoritmo):
    """
        Implementação do algoritmo Best Fit para alocação dinâmica de memória.

        A estratégia consiste em percorrer toda a memória simulada em busca do
        menor bloco livre que seja capaz de acomodar o tamanho solicitado.
        O objetivo é reduzir a fragmentação externa, evitando o uso de blocos
        livres excessivamente grandes.
    """

    def procura_bloco_livre(self, mem: list[Byte], tam_bloco: int, id: int) -> int:
         """
            Procura o menor bloco livre possível e realiza a alocação diretamente na estrutura de memória.

            :param mem: Lista que representa a memória física simulada.
            :param tam_bloco: Tamanho do bloco a ser alocado.
            :param id: Identificador único do bloco alocado.
            :return: Índice inicial do bloco alocado ou -1 caso não exista espaço.
         """
        i = 0
        min_idx_ini = -1
        min_tam_possivel = len(mem) + 1

        # Percorre a memória identificando regiões livres contíguas
        while i < len(mem):
            # Se o byte pertence a um bloco alocado, pula diretamente para o próximo bloco
            if mem[i].idx_ini > -1:
                i += mem[i].tam
            else:
                # Identifica o tamanho do bloco livre a partir da posição atual
                idx_ini = i
                tam_possivel = 1
                while idx_ini + tam_possivel < len(mem) and mem[idx_ini + tam_possivel].id == -1:
                    tam_possivel += 1
                # Atualiza o menor bloco livre viável
                if tam_possivel >= tam_bloco and tam_possivel < min_tam_possivel:
                    min_idx_ini = idx_ini
                    min_tam_possivel = tam_possivel
                i += tam_possivel
        # Realiza a alocação caso um bloco adequado tenha sido encontrado
        if min_tam_possivel >= tam_bloco:
            for i in range(min_idx_ini, min_idx_ini + tam_bloco):
                mem[i].id = id
                mem[i].idx_ini = min_idx_ini
                mem[i].tam = tam_bloco
            return min_idx_ini
        return min_idx_ini