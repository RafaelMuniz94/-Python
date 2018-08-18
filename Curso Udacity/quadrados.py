import turtle
import random as rand

def desenhar_quadrado(jeguinha,angulo):
    #for p in range(0,2):
    jeguinha.forward(rand.randint(0,50))
    jeguinha.right(angulo)
    jeguinha.forward(rand.randint(0,50))





window = turtle.Screen()
window.bgcolor('red')
window.mainloop()
jeguinha = turtle.Turtle()
jeguinha.speed(50)
for z in range(1,1000000000000):
    #desenhar_quadrado(jeguinha,z)
    desenhar_quadrado(jeguinha, rand.randint(-90,90))

window.exitonclick()

