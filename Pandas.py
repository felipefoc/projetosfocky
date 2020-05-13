import pandas as pd
import time

a = 1
db = pd.read_excel("BANCODEDADOS.XLSX")
dbdict = dict(sorted(db.values.tolist()))
list_valor = []
list_prod = []
qnt_prod = []
writer = pd.ExcelWriter('ComprasFinal.xlsx', engine='xlsxwriter')


print('Seja bem vindo ! Em poucos segundos os produtos disponíveis apareceram abaixo... \nPara adicionar um '
      'produto ao carrinho é muito simples, basta escrever o nome do "PRODUTO" seguir com o enter e fazer o'
      ' mesmo com a "QUANTIDADE"\nQualquer dúvida pode entrar em contato conosco pelo whatsapp'.upper())
time.sleep(4)

def valorfinal(var_soma=0):  # Calcula o valor final de toda a compra.
    for valor in list_valor:
        var_soma += valor
    print('Total : R$',var_soma)
    es = pd.DataFrame({'Qntd': qnt_prod,
                        'Prod': list_prod,
                        'Valor': list_valor})
    es.to_excel(writer, sheet_name='log')
    writer.save()  # Exporta os dados para o Excel.


def produtos():  # Cardápio
    print('-'*40)
    print(db)
    print('-'*40)
    print('Qual produto deseja comprar ?'.upper())
    if a == 1:
        x = input('Produto : ').upper()
        try:
            qnt = int(input('Quantidade : '))
        except ValueError:
            print('ERROR : Digite a quantidade em forma numérica'.upper())
            time.sleep(2)
            produtos()
        if x in dbdict:
            list_valor.append(dbdict[x] * qnt)
            list_prod.append(x)
            qnt_prod.append(qnt)
            print('Produto selecionado : {}({})\nValor : R$ {:.2f}'.format(x, qnt, dbdict[x] * qnt).upper())
            keep = str(input('Continuar comprando ou finalizar compra ? ')).upper()
            if keep == 'CONTINUAR COMPRANDO':
                produtos()
            elif keep == 'FINALIZAR COMPRA':
                valorfinal()
            else:
                print('Comando não encontrado, finalizando compra.')
                valorfinal()
        elif x not in dbdict:
            print('Produto não encontrado ou quantidade inválida, tente novamente.'.upper())
            produtos()


produtos()
