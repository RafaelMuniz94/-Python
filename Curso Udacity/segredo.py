import time
import os

def renomear_arquivos(pasta):
    print('Começou a Procurar os arquivos em ',pasta)
    file_list = os.listdir(pasta)
    os.chdir(pasta)
    print('Foram encontrados: ',len(file_list),' arquivos')
    

    print('Começou a Renomear:',time.ctime())

    for file_name in file_list:
        nomeAtual = file_name
        mt = str.maketrans(dict.fromkeys('0123456789'))  #é necessário o uso desse cara para python 3
        nomeFinal = file_name.translate(mt) #recebe uma tabela de translação e uma lista de caracteres a serem removidos)
        print('Renomeando ',nomeAtual,' para ', nomeFinal)

        
        os.rename(nomeAtual,nomeFinal) 
    
    print('Terminou de Renomear:', time.ctime())

#pasta = r'S:\Dev\Python\Curso Udacity\Fotos\prank'
pasta = r'S:\Dev\Python\Curso Udacity\Fotos\prank2'## r = rawpack (sera usado como estiver e não interpretado)
renomear_arquivos(pasta)
