import os

def consolidar_arquivos_texto(diretorio, arquivo_saida):
    try:
        with open(arquivo_saida, 'w') as arquivo_final:
            for nome_arquivo in os.listdir(diretorio):
                if nome_arquivo.endswith('.txt'):
                    with open(os.path.join(diretorio, nome_arquivo), 'r') as arquivo_atual:
                        arquivo_final.write(arquivo_atual.read())
                        arquivo_final.write('\n')
        print("Arquivos consolidados com sucesso!")
    except Exception as e:
        print("Ocorreu um erro ao consolidar os arquivos:", str(e))

diretorio = 'caminho/para/seu/diretorio'
arquivo_saida = 'arquivo_consolidado.txt'
consolidar_arquivos_texto(diretorio, arquivo_saida)
