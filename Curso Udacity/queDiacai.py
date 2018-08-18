import datetime


def diaSemana(dia):
    if(dia == 0):
        return 'Segunda'
    elif(dia == 1):
        return 'Terça'
    elif(dia == 2):
        return 'Quarta'
    elif(dia == 3):
        return 'Quinta'
    elif(dia == 4):
        return 'Sexta'
    elif(dia == 5):
        return 'Sabado'
    else:
        return 'Domingo'

dia = int(input('Digite um dia:'))
mes = int(input('Digite um mes:'))

hoje = datetime.datetime.now()

count = 0
while( count < 100):
    if(hoje.month == mes and hoje.day == dia):
        print(hoje.strftime('%d/%m/%Y'), ' - ', diaSemana(hoje.weekday()))
        count += 1
    hoje += datetime.timedelta(days=1)

