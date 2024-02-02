"""
E07: Calcular la hipotenusa de un triángulo, teniendo como base el valor del cateto 1 y 2 que serán
dados por el usuario. Para esto debe de hacer uso del Teorema de Pitágoras en el cálculo de la
hipotenusa teniendo los catetos. (h= √(a^2 )+b^2) no se debe hacer uso de la librería Math.hypot
"""


from rich import print
from utils_adso import texto_es_num_float, create_tabla


def hipotenusa(cate1: float, cate2: float) -> float:
    h = ((cate1**2)+cate2**2)**0.5
    return h


def ej07():
    while True:
        create_tabla(titulo="Hallar Hipotenusa de Triangulo")
        print("  [bold cyan]Ingrese cateto 1: ", end="")
        cate1 = texto_es_num_float(input())
        print("  [bold cyan]Ingrese cateto 2: ", end="")
        cate2 = texto_es_num_float(input())
        print(f"\n   [bold green]La hipotenusa del triangulo es: {hipotenusa(cate1, cate2)}\n\n")
        print("[yellow]Presione una tecla para volver al menú...")
        return input()
