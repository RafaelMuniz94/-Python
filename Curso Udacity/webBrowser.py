import webbrowser
import time


##for p in range(0,3):
pausa = 0
print('Hora de Inicio: '+ time.ctime())
while pausa < 3:
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=8gVrm3GtORY')
    pausa += 1
    print(pausa,"ª pausa: "+ time.ctime())

