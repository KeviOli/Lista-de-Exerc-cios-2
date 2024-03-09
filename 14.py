import csv

def ler_arquivo_csv(nome_arquivo):
    try:
        with open(nome_arquivo, newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            linhas = list(leitor_csv)
        return linhas
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado.".format(nome_arquivo))
    except Exception as e:
        print("Ocorreu um erro ao ler o arquivo CSV:", str(e))

nome_arquivo_csv = 'exemplo.csv'
linhas_csv = ler_arquivo_csv(nome_arquivo_csv)
if linhas_csv:
    print("Conteúdo do arquivo CSV:")
    for linha in linhas_csv:
        print(linha)
