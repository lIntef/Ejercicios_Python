"""
    E02: En este problema tenemos un único dato de entrada: un valor numérico entero que deberá
    ingresar el usuario. La salida del algoritmo será informar si el usuario ingresó un valor par o impar.
    Sabemos que un número par es aquel que es divisible por 2 o, también, que un número es par si el
    valor residual que se obtiene al dividirlo por 2 es cero. Según lo anterior, podremos informar que
    el número ingresado por el usuario es par si al dividirlo por 2 obtenemos un resto igual a cero. De
    lo contrario, informaremos que el número es impar.
"""


from rich import print
from utils_adso import texto_es_num_int, create_tabla


def par_impar(num: int) -> bool:
    return num % 2 == 0


def ej02():
    while True:
        create_tabla(titulo="Hallar si el Numero es Par o Impar")
        print("  [bold cyan]Ingrese un numero: ", end="")
        num = texto_es_num_int(input())
        print(f"\n   [bold green]El numero es: " + ("par\n\n" if par_impar(num) else "impar\n\n"))
        print("[yellow]Presione una tecla para volver al menú...")
        return input()
