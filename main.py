from classes.alg_impl.BestFit import BestFit
from classes.alg_impl.FirstFit import FirstFit
from classes.alg_impl.WorstFit import WorstFit
from classes.Algoritmo import Algoritmo
from classes.Byte import Byte
from classes.Alocador import Alocador

alocador = Alocador()
best_fit = BestFit()
first_fit = FirstFit()
worst_fit = WorstFit()

while True:
    entrada = input("> ").split()

    match entrada[0]:
        case "init":
            alocador.init(int(entrada[1]))
            pass

        case "alloc":
            match entrada[2]:
                case "first":
                    if alocador.alloc(int(entrada[1]), first_fit):
                        print("Alocação realizada com sucesso")
                    else:
                        print("Erro na alocação")
                    pass
                case "best":
                    if alocador.alloc(int(entrada[1]), best_fit):
                        print("Alocação realizada com sucesso")
                    else:
                        print("Erro na alocação")
                    pass
                case "worst":
                    if alocador.alloc(int(entrada[1]), worst_fit):
                        print("Alocação realizada com sucesso")
                    else:
                        print("Erro na alocação")
                    pass
                case _ :
                    print("Algoritmo inválido")
                    pass

        case "freeid":
            if alocador.free_id(int(entrada[1])):
                print("Memória liberada com sucesso")
            else:
                print("Erro na liberação de memória")
            pass

        case "chooseblock":
            match entrada[2]:
                case "first":
                    if not alocador.choose_block(int(entrada[1]), first_fit):
                        print("Erro na busca pelo bloco")
                    pass
                case "best":
                    if not alocador.choose_block(int(entrada[1]), best_fit):
                        print("Erro na busca pelo bloco")
                    pass
                case "worst":
                    if not alocador.choose_block(int(entrada[1]), worst_fit):
                        print("Erro na busca pelo bloco")
                    pass
                case _ :
                    print("Algoritmo inválido")
                    pass

        case "show":
            alocador.show()
            pass

        case "stats":
            alocador.stats()
            pass

        case "exit":
            break

        case _ :
            print("Comando inválido")