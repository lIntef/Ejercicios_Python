"""
E11: Dado un número entero leído por pantalla, muestre cada uno de los dígitos del número en
orden inverso. Ej: Si el número es 324, se debe mostrar 4, 2, 3.
"""


from rich import print
from utils_adso import texto_es_num_int, create_tabla


def invertir(num: int) -> str:
    vari = []
    lista = ""
    for i in range(0, len(str(num))):
        vari.append(str(num)[i])
    vari.sort(reverse=True)
    for i in range(0, len(str(num))):
        lista = lista + vari[i]
    return lista


def ej11():
    while True:
        create_tabla(titulo="Mostrar Numeros en Orden Inverso")
        print("  [bold cyan]Ingrese un numero: ", end="")
        num = texto_es_num_int(input())
        print(f"\n   [bold green]El numero invertido es: {invertir(num)}\n\n")
        print("[yellow]Presione una tecla para volver al menú...")
        return input()
