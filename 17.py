import csv

def mes_com_mais_vendas(arquivo_csv):
    vendas_por_mes = {}
    try:
        with open(arquivo_csv, newline='') as csvfile:
            leitor_csv = csv.reader(csvfile)
            next(leitor_csv)
            for linha in leitor_csv:
                if len(linha) == 2:
                    mes = linha[0]
                    try:
                        vendas = int(linha[1])
                    except ValueError:
                        print("Valor de vendas inválido na linha:", linha)
                        continue
                    vendas_por_mes[mes] = vendas
                else:
                    print("A linha não tem o formato esperado:", linha)
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado.".format(arquivo_csv))
        return None
    except Exception as e:
        print("Ocorreu um erro ao ler o arquivo CSV:", str(e))
        return None
    
    mes_mais_vendas = max(vendas_por_mes, key=vendas_por_mes.get)
    return mes_mais_vendas

arquivo_csv = 'vendas.csv'
mes = mes_com_mais_vendas(arquivo_csv)
if mes:
    print("O mês com mais vendas é:", mes)
