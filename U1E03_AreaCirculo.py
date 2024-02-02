""""
    E03: En este problema debemos de definir una constante con el valor de PI como 3,1416 y
    tenemos un único dato de entrada dado por el usuario: un valor numérico que puede ser entero o
    flotante que indicara el radio de un círculo. La salida del algoritmo será el área del circulo teniendo
    en cuenta que A=PI*r^2. Si el usuario ingresó valor negativo o cero tendremos que emitir un
    mensaje informando las causas por las cuales no se podrá efectuar la operación.
"""


from rich import print
from utils_adso import texto_es_num_float, create_tabla
import math


def area_circulo(num: int | float) -> float:
    return math.pi * (num**2)


def ej03():
    while True:
        create_tabla(titulo="Hallar Area de un Circulo")
        print("  [bold cyan]Ingrese un numero: ", end="")
        num = texto_es_num_float(input())
        print(f"\n  [bold yellow]El numero debe ser mayor a cero\n\n" if num <= 0
              else f"\n   [bold green]El area es {area_circulo(num)}\n\n")
        print("[yellow]Presione una tecla para volver al menú...")
        return input()
