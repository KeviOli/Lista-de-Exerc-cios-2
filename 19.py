import csv

def soma_vendas_por_vendedor(arquivo_csv):
    vendas_por_vendedor = {}
    try:
        with open(arquivo_csv, newline='') as csvfile:
            leitor_csv = csv.reader(csvfile)
            next(leitor_csv)
            for linha in leitor_csv:
                if len(linha) == 2:
                    vendedor = linha[0]
                    try:
                        valor_venda = float(linha[1])
                    except ValueError:
                        print("Valor de venda inválido na linha:", linha)
                        continue
                    if vendedor in vendas_por_vendedor:
                        vendas_por_vendedor[vendedor] += valor_venda
                    else:
                        vendas_por_vendedor[vendedor] = valor_venda
                else:
                    print("A linha não tem o formato esperado:", linha)
    except FileNotFoundError:
        print("O arquivo '{}' não foi encontrado.".format(arquivo_csv))
        return None
    except Exception as e:
        print("Ocorreu um erro ao ler o arquivo CSV:", str(e))
        return None
    
    return vendas_por_vendedor

arquivo_csv = 'vendas1.csv'
vendas_por_vendedor = soma_vendas_por_vendedor(arquivo_csv)
if vendas_por_vendedor:
    print("Soma de vendas por vendedor:")
    for vendedor, soma_vendas in vendas_por_vendedor.items():
        print(f"{vendedor}: R${soma_vendas:.2f}")
