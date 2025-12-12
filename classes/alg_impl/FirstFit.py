from classes.Algoritmo import Algoritmo
from classes.Byte import Byte


class FirstFit(Algoritmo):

    def procura_bloco_livre(self, mem: list[Byte], tam_bloco: int, id: int) -> int:
        i = 0
        while i < len(mem):
            if mem[i].idx_ini > -1:
                i += mem[i].tam
            else:
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