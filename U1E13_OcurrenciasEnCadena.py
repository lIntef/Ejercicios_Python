"""
E13: Desarrollar un algoritmo que reciba como entrada un carácter y de cómo salida el número de
ocurrencias de dicho carácter en una cadena de caracteres
"""

from rich import print
from utils_adso import create_tabla


def verificacion(word: str, lett: str) -> int:
    cant = 0
    for i in range(0, len(word)):
        if word[i] == lett:
            cant += 1
    return cant


def ej13():
    while True:
        create_tabla(titulo="Numero de Ocurrencia de un caracter en una Cadena")
        print("  [bold cyan]Ingrese una palabra: ", end="")
        word = input()
        print("  [bold cyan]Ingrese el caracter de ocurrencia: ", end="")
        lett = input()
        print("\n   [b green]El caracter {lett} tiene una ocurrencia de "
              f"{verificacion(word, lett)} en la cadena {word}\n\n"
              if len(lett) == 1 else "\n   [yellow]Lo siento, Ingresó mas de un caracter\n\n")
        print("[yellow]Presione una tecla para volver al menú...")
        return input()
