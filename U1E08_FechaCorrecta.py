"""
E08: ingresa un valor numérico de 8 dígitos que representa una fecha con el siguiente formato:
aaaammdd verificar si la fecha es correcta en sentido de numero de meses y días
"""

from rich import print
from utils_adso import texto_es_num_int, create_tabla


def separar_fecha(num: int) -> []:
    anio = int(num / 10000)
    mes = int(num % 10000 / 100)
    dia = int(num % 100)
    vari = [anio, mes, dia]
    return vari


def ej08():
    while True:
        create_tabla(titulo="Ingreso de Fecha")
        print("  [bold cyan]Ingrese un valor numerico de 8 dígitos: ", end="")
        num = texto_es_num_int(input())
        resto = separar_fecha(num)
        res = print(f"\n   [green]El año es {resto(num)[0]}, el mes {resto(num)[1]} y el dia es: "
                    f"{resto(num)[2]}") if ((1000 <= resto(num)[0] <= 2024)
                                            and (1 <= resto(num)[1] <= 12)
                                            and (1 <= resto(num)[2] <= 30)) \
            else print("\n   [b yellow]La fecha no existe")
        res if len(str(num)) == 8 else print("\n   [red]La cantidad de dígitos es inaceptable")
        print("\n[yellow]Presione una tecla para volver al menú...")
        return input()
