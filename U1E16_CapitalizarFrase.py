"""
E16: Desarrollar un algoritmo que solicite una frase de mínimo 5 palabras y capitalizar la cadena.
"""


from rich import print
from utils_adso import texto_es_num_int, create_tabla


def capitalizar(txt: str) -> str:
    txt_cap = txt.title()
    return txt_cap


def ej16():
    while True:
        create_tabla(titulo="Solicitar una Frase Mínimo de 5 Palabras y Capitalizar la Cadena")
        print("  [bold cyan]Ingrese una frase: ", end="")
        txt = (input())
        print(f"\n   [bold gray]La Frase Capitalizada es: {capitalizar(txt)}\n\n")
        print("[yellow]Presione una tecla para volver al menú...")
        return input()
