"""
E14: Desarrollar un algoritmo que determine si una cadena de caracteres es palíndroma. Una
cadena se dice palíndromo si al invertirla es igual a ella misma.
"""


from rich import print
from utils_adso import texto_es_num_int, create_tabla


def verificacion(txt: str) -> bool:
    vari = []
    lista = ""
    lista2 = ""
    for i in range(0, len(txt)):
        vari.append(txt[i])
    for i in range(0, len(txt)):
        lista = lista + vari[i]
    vari.reverse()
    for i in range(0, len(txt)):
        lista2 = lista2 + vari[i]
    return lista == lista2


def ej14():
    while True:
        create_tabla(titulo="Comprobar si una palabra es palindroma")
        print("  [bold cyan]Ingrese una palabra: ", end="")
        txt = input()
        print("\n   [b green]Es Palíndroma \n\n" if verificacion(txt) else "\n   [b green]No es Palíndroma\n\n")
        print("[yellow]Presione una tecla para volver al menú...")
        return input()
