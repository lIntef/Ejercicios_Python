from rich import print
from rich import box
from rich.table import Table
import os


def create_tabla(titulo: str):
    os.system("cls")
    table = Table(show_header=True, header_style="blue")
    table.title = (
        "\n\n[magenta]Bienvenido al desarrollo de lógica con Python\n"
        "[magenta]Edwin Alexander Correa Aullon\n"
        "[magenta]2670142\n"
    )
    table.add_column(titulo, justify="center")
    for box_style in [
        box.SQUARE,
        box.MINIMAL,
        box.SIMPLE,
        box.SIMPLE_HEAD,
    ]:
        table.box = box_style
        table.border_style = "bold blue"
        table.width = 75
    print(table)


def texto_es_num_int(valor: str) -> int:
    while True:
        try:
            return int(valor)
        except:
            print(f"   [red]{valor} no es un dato valido")
            print("   [yellow]Ingresa nuevamente un numero", end="")
            valor = input()


def texto_es_num_float(valor: str) -> float:
    while True:
        try:
            return float(valor)
        except:
            print(f"   [red]{valor} no es un dato valido")
            print("   [yellow]Ingresa nuevamente un numero", end="")
            valor = input()
