"""
E06: Leer tres valores numéricos enteros, indicar cuál es el mayor, cuál es el del medio y cuál, el
menor. Considerar que los tres valores serán diferentes.
"""


from rich import print
from utils_adso import texto_es_num_int, create_tabla


def verificación(num1: int, num2: int, num3: int) -> []:
    vari = [num1, num2, num3]
    vari.sort()
    return vari


def ej06():
    while True:
        create_tabla(titulo="Indicar Numero Mayor, del Medio y Menor")
        print("  [bold cyan]Ingrese primer numero: ", end="")
        num1 = texto_es_num_int(input())
        print("  [bold cyan]Ingrese segundo numero: ", end="")
        num2 = texto_es_num_int(input())
        print("  [bold cyan]Ingrese tercer numero: ", end="")
        num3 = texto_es_num_int(input())
        res = verificación(num1, num2, num3)
        print(f"   [green]El numero mayor es: {res[2]}\n   "
              f"El numero de en medio es: {res[1]}\n   "
              f"El numero menor es: {res[0]}")
        print("[yellow]Presione una tecla para volver al menú...")
        return input()
