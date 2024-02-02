"""
    E04: En este problema tenemos un único dato de entrada: un valor numérico entero que deberá
    ingresar el usuario. La salida del algoritmo será informar si el numero ingresado por el usuario es
    múltiplo de 2 y 3. Sabemos que un número es múltiplo de otro cuando al dividir estos dos
    números el residuo sea 0. Si el usuario ingresó un valor negativo o cero tendremos que emitir un
    mensaje informando las causas por las cuales no se podrá efectuar la operación
"""


from rich import print
from utils_adso import texto_es_num_int, create_tabla


def comprobacion(num: int) -> bool:
    return num % 2 == 0 and num % 3 == 0


def ej04():
    while True:
        create_tabla(titulo="Hallar si el numero es Multiplo de Dos y Tres")
        print("  [bold cyan]Ingrese un numero: ", end="")
        num = texto_es_num_int(input())
        print("\n   [b green]El numero " + str(num) + (" SI " if comprobacion(num) else " NO ")
              + "es un multiplo de dos y tres\n\n")
        print("[yellow]Presione una tecla para volver al menú...")
        return input()
