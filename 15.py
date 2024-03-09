import json

def ler_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo) as arquivo_json:
            dados = json.load(arquivo_json)
        return dados
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado.".format(nome_arquivo))
    except json.JSONDecodeError as e:
        print("Ocorreu um erro ao decodificar o JSON:", str(e))
    except Exception as e:
        print("Ocorreu um erro ao ler o arquivo JSON:", str(e))

nome_arquivo_json = 'exemplo.json'
dados_json = ler_arquivo_json(nome_arquivo_json)
if dados_json:
    print("Conteúdo do arquivo JSON:")
    print(dados_json)
