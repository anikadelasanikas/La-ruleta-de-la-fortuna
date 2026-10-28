import turtle
import random

print("Acérquense a la Ruleta de la fortuna")
print("Oh, bienvenido cliente")

ventana = turtle.Screen()
ventana.title("Ruleta de la Fortuna")

ruleta = turtle.Turtle()
ruleta.shape("circle")
ruleta.color("red")
ruleta.shapesize(5)
ruleta.penup()


def girar_ruleta(x, y):
    numero_aleatorio = random.randint(1, 100)

    print("\nLa ruleta está girando...")
    print("Ha salido el número:", numero_aleatorio)

    comprobar_premio(numero_aleatorio)


def comprobar_premio(numero_aleatorio):

    if numero_aleatorio <= 10:
        print("Qué pena, has perdido")

    elif numero_aleatorio <= 20:
        print("¡Felicidades! Ganaste un pez")

    elif numero_aleatorio <= 45:
        print("¡Genial! Has ganado un peluche")
        print("Ejem, ejem... así viene de fábrica")
        print("No se preocupe, es normal")

    elif numero_aleatorio <= 70:
        print("¿Cómo es posible? ¡No estaba trucada!")
        print("Eh... quiero decir, tome su premio")

    else:
        print("¡Felicidades! Ganó un viaje a mi cerro")


ruleta.onclick(girar_ruleta)

ventana.mainloop()
