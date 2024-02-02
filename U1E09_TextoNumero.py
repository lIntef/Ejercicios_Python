"""
E09: Se debe de ingresar un numero comprendido entre 1 y 12 por el usuario. El algoritmo debe
de imprimir el mes correspondiente en texto.
"""


from rich import print
from utils_adso import texto_es_num_int, create_tabla


def hallar_mes(num: int) -> str:
    if num == 1:
        return "Enero"
    elif num == 2:
        return "Febrero"
    elif num == 3:
        return "Marzo"
    elif num == 4:
        return "Abril"
    elif num == 5:
        return "Mayo"
    elif num == 6:
        return "Junio"
    elif num == 7:
        return "Julio"
    elif num == 8:
        return "Agosto"
    elif num == 9:
        return "Septiembre"
    elif num == 10:
        return "Octubre"
    elif num == 11:
        return "Noviembre"
    elif num == 12:
        return "Diciembre"


def ej09():
    while True:
        create_tabla(titulo="Imprimir el Mes en Texto del Numero Seleccionado")
        print("  [bold cyan]Ingrese un numero del 1 al 12: [/bold cyan]", end="")
        num = texto_es_num_int(input())
        print(f"\n   [b green]El mes {num} es: {hallar_mes(num)}\n\n" if 1 <= num <= 12 else "\n   [red]El mes no existe\n\n")
        print("[yellow]Presione una tecla para volver al menú...")
        return input()
