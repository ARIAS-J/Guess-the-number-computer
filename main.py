# Guess the number computer
import random


def adivina_computador(x):

    print("======================")
    print(" Bienvenido al Juego! ")
    print("======================")

    print(f"Elige un numero entre 1 y {x} para que el computador adivine el numero.")

    limite_inferior = 1
    limite_superior = x

    respuesta_usuario = ""

    while respuesta_usuario != "v":

        # Prediccion.
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)

        else:
            # si ambos son iguales.
            prediccion = limite_superior # tambien se podria utilizar limite_inferior ya que ambos son iguales.

        # Obteniendo respuesta del usuario.
        respuesta_usuario = input("\n"f"Mi Prediccion es {prediccion}. Si es muy alta, Ingresa (A). Si es muy baja, Ingresa(B). "
                                  f"Si es verdadera, Ingresa(V)").lower()

        # condicional de respuesta.
        if respuesta_usuario == "a":
            limite_superior = prediccion - 1
        elif respuesta_usuario == "b":
            limite_inferior == prediccion + 1

    print("\n"f"El computador adivino el numero correctamente: {prediccion}")


adivina_computador(100)