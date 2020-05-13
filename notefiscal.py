# Projeto NOTA FISCAL
from datetime import datetime, timedelta


def preventrega():
    x = datetime.today() + timedelta(minutes=40)
    x = str(x)
    print('Entrega prevista :', x[11:16])


def datahora():
    now = datetime.now()
    print('Data: {}/{}/{} Hora: {}:{}:{}'.format(now.day, now.month, now.year, now.hour, now.minute,
                                                 now.second))


rest = {'nome': 'Comidas do zé', 'bairro': 'Maracanã', 'rua': 'Avenida Maracana', 'tel': '(21)96692-9828'}
print('Projeto NOTA FISCAL\n'.center(30).upper())
print('Restaurante: {}\nBairro: {}\nRua: {}'.format(rest['nome'], rest['bairro'], rest['rua']).upper())
print('whatsapp: {}'.format(rest['tel']).upper())
datahora()
preventrega()
