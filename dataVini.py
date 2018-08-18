import datetime as date

msg = 'Vini seu otário, bora breja dia '



hoje = date.datetime.now()
while(hoje.year < 2201):
          if(hoje.weekday() == 4 and hoje.day == 24 and hoje.month == 9): # weekday começa na segunda com 0 e vai até domingo com 6
            #print(msg, hoje.strftime('%d/%m/%Y'),"?") #strftime equivale a toString para date
            print(hoje.strftime('%d/%m/%Y'))  # strftime equivale a toString para date
          hoje += date.timedelta(days=1) # como incrementar o dia
        
