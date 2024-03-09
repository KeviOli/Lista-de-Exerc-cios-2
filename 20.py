import csv

def vendedor_mais_e_menos_vendeu(arquivo_csv):
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
    
    vendedor_mais_vendeu = max(vendas_por_vendedor, key=vendas_por_vendedor.get)
    vendedor_menos_vendeu = min(vendas_por_vendedor, key=vendas_por_vendedor.get)
    
    return vendedor_mais_vendeu, vendedor_menos_vendeu

arquivo_csv = 'vendas2.csv'
vendedor_mais, vendedor_menos = vendedor_mais_e_menos_vendeu(arquivo_csv)
if vendedor_mais and vendedor_menos:
    print("Vendedor que mais vendeu:", vendedor_mais)
    print("Vendedor que menos vendeu:", vendedor_menos)
