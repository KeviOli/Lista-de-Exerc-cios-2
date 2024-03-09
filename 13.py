def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado.".format(nome_arquivo))
    except Exception as e:
        print("Ocorreu um erro ao ler o arquivo:", str(e))

nome_arquivo = 'exemplo.txt'
conteudo = ler_arquivo(nome_arquivo)
if conteudo:
    print("Conteúdo do arquivo:")
    print(conteudo)
