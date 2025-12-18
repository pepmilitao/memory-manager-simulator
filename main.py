from classes.alg_impl.BestFit import BestFit
from classes.alg_impl.FirstFit import FirstFit
from classes.alg_impl.WorstFit import WorstFit
from classes.Algoritmo import Algoritmo
from classes.Byte import Byte
from classes.Alocador import Alocador

def ajuda():
    print("\nComandos disponíveis:")
    print("  help                  mostra esta mensagem")
    print("  exit                  encerra o simulador")
    print("  init <tamanho>        inicializa a memória com tamanho (em bytes)")
    print("  alloc <tam> <alg>     aloca bloco de memória de <tam> usando algoritmo:")
    print("                        first | best | worst")
    print("  freeid <id>           libera o bloco com identificador <id>")
    print("  show                  exibe o mapa atual de uso da memória")
    print("  stats                 mostra estatísticas de uso e fragmentação\n")

print("Bem-vindo ao Memto - Simulador de Gerência de Memória :)\n")
print("Digite 'help' para ver os comandos disponíveis.\n")

alocador = Alocador()
algoritmos = {
    'first': FirstFit(),
    'best': BestFit(),
    'worst': WorstFit()
}
best_fit = BestFit()
first_fit = FirstFit()
worst_fit = WorstFit()

while True:
    entrada = input("[Memto]> ").split()

    match entrada[0]:
        case "help" | "?":
            ajuda()
        case "exit" | "quit":
            print("Encerrando simulador.")
            break
        case "init":
            if len(entrada) < 2:
                print("Erro: use 'init <tamanho>', ex: init 64")
                continue
            alocador.init(int(entrada[1]))
            print(f"Memória inicializada com {entrada[1]} bytes.")
            pass

        case "alloc":
            if len(entrada) < 3:
                print("Erro: use 'alloc <tam> <alg>', ex: alloc 8 best")
                continue
            match entrada[2]:
                case "first":
                    sucesso = alocador.alloc(int(entrada[1]), first_fit)
                case "best":
                    sucesso = alocador.alloc(int(entrada[1]), best_fit)
                case "worst":
                    sucesso = alocador.alloc(int(entrada[1]), worst_fit)
                case _:
                    print("Algoritmo inválido (use: first | best | worst).")
                    continue
            if sucesso:
                print("Alocação realizada com sucesso")
            else:
                print("Erro na alocação: espaço insuficiente ou memória não inicializada")

        case "freeid":
            if len(entrada) < 2:
                print("Erro: use 'freeid <id>', ex: freeid 2")
                continue
            if alocador.free_id(int(entrada[1])):
                print("Memória liberada com sucesso")
            else:
                print("Erro na liberação de memória (id inválido)")

        case "chooseblock":
            if len(entrada) < 3:
                print("Erro: use 'chooseblock <tam> <alg>', ex: chooseblock 8 worst")
                continue
            match entrada[2]:
                case "first":
                    bloco = alocador.choose_block(int(entrada[1]), first_fit)
                case "best":
                    bloco = alocador.choose_block(int(entrada[1]), best_fit)
                case "worst":
                    bloco = alocador.choose_block(int(entrada[1]), worst_fit)
                case _:
                    print("Algoritmo inválido (use: first | best | worst).")
                    continue
            print(f"Bloco sugerido: {bloco}")

        case "show":
            alocador.show()
        case "stats":
            alocador.stats()
        case _:
            print("Comando inválido. Digite 'help' para ver os comandos.")