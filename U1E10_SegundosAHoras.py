"""
E10: Dado un número (leído por teclado), que representa los segundos que ha invertido una
persona en hacer un examen, determinar cuántas horas, minutos y segundos ha invertido.
Imprima el resultado por pantalla.

"""


from rich import print
from utils_adso import texto_es_num_int, create_tabla


def conversion(num: int) -> []:
    horas = num / 3600
    minutos = (num % 3600) / 60
    segundos = (minutos % 1) * 60
    res = (int(round(horas)), int(round(minutos)), int(round(segundos)))
    return res


def ej10():
    while True:
        create_tabla(titulo="Convertir Segundos Totales en Horas, Minutos y Segundos")
        print("  [b cyan]Ingrese segundos: ", end="")
        num = texto_es_num_int(input())
        res = conversion(num)
        print(f"\n   [b green]{res[0]} horas\n   {res[1]} minutos\n   {res[2]} segundos\n\n")
        print("[yellow]Presione una tecla para volver al menú...[/yellow]")
        return input()
