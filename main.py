from paises import *

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("## Bem vindo ao sistema de países ##")
        print("Uso: python main.py <ação> <nome do país>")
        print("Ações disponíveis: contagem, moeda, populacao")
    else:
        argumento1 = sys.argv[1]

        if argumento1 == "contagem":
            numero_de_paises = contagem_de_paises()
            print("Existem {} países no mundo todo".format(numero_de_paises))
        elif argumento1 == "moeda":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_moedas(pais)
        elif argumento1 == "populacao":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print("Argumento inválido")