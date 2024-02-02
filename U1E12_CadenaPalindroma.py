"""
E12: Se debe de ingresar un numero por el usuario, este debe de ser evaluado para verificar que el
número de cifras sea par y verificar si el número es capicúa o no.
"""


from rich import print
from utils_adso import texto_es_num_int, create_tabla


def verificacion(num: int) -> bool:
    vari = []
    lista = ""
    lista2 = ""
    for i in range(0, len(str(num))):
        vari.append(str(num)[i])
    for i in range(0, len(str(num))):
        lista = lista + vari[i]
    vari.reverse()
    for i in range(0, len(str(num))):
        lista2 = lista2 + vari[i]
    return lista == lista2


def ej12():
    while True:
        create_tabla(titulo="Comprobar si un numero es capicúa")
        print("  [bold cyan]Ingrese un numero: ", end="")
        num = texto_es_num_int(input())
        if (len(str(num)) % 2) == 0:
            print("\n   [b green]Es Capicúa \n\n" if verificacion(num) else "\n   [b green]No es Capicúa\n\n")
        else:
            print("\n   [b yellow]Lo siento, El numero de cifras de dato digitado no es par\n\n")
        print("[yellow]Presione una tecla para volver al menú...")
        return input()
