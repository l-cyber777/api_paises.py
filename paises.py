import json
import sys

import requests

URL_ALL = "https://restcountries.eu/rest/v2/all"
URL_NAME = "https://restcountrutries.eu/rest/v2/name"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print("Erro ao fazer requisição em:", url)

def parsing(texto_da_reposta):
    try:
        return json.loads(texto_da_reposta)     ##PARSING DE JSON
    except:
        print("Erro ao fazer parsing")

def contagem_de_paises(lista_de_paises):
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            return len(lista_de_paises)

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])

def mostrar_populacao(nome_do_pais):
    resposta = requisicao("{}/{}".format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print("{}:{} habitantes".format(pais['name'], pais['population']))

def mostrar_pupulacao(nome_do_pais):
    resposta = requisicao("{}/{}".format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print("{}: {} habitantes".format(pais['name'], pais['pupulation']))
    else:
        print("Pais não encontrado")

def mostrar_moedas(nome_do_pais):
    resposta = requisicao("{}/{}".format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print("Moedas", pais['name'])
                moedas = pais['currencies']
                for moeda in moedas:
                    print("{} - {}".format(moeda['name'], moeda['code']))

def ler_nome_do_pais():
    try:
        nome_do_pais = sys.argv[2]
        return nome_do_pais
    except:
        print("É preciso passar o nome do país")