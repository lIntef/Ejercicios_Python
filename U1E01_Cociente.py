"""
    E01: En este problema, los datos de entrada son los dos valores enteros que ingresará el usuario a
    través del teclado (los llamaremos a y b) y la salida será su cociente (un número flotante). Ahora
    bien, existe la posibilidad de que el usuario ingrese como segundo valor el número 0 (cero). En
    este caso, no podremos mostrar el cociente ya que la división por cero es una indeterminación, así
    que tendremos que emitir un mensaje informando las causas por las cuales no se podrá efectuar
    la operación.
"""


from rich import print
from utils_adso import texto_es_num_int, create_tabla


def cociente(num1: int, num2: int) -> float:
    if num2 == 0:
        return 0
    else:
        return round(num1 / num2, 2)


def ej01():
    while True:
        create_tabla(titulo="Calcular Cociente Numerico")
        print("  [bold cyan]Ingrese el primer numero: ", end="")
        num1 = texto_es_num_int(input())
        print("  [bold cyan]Ingrese el segundo numero: ", end="")
        num2 = texto_es_num_int(input())
        res = cociente(num1, num2)
        print(f"\n   [bold green]El resultado es {res}\n\n" if res != 0
              else "\n   [yellow]No se puede operar por 0\n\n")
        print("[yellow]Presione una tecla para volver al menú...")
        return input()
