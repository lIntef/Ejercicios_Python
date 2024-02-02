"""
E15: Pedir un número de 0 a 99 y mostrarlo escrito. Por ejemplo, para 56 mostrar: cincuenta y
seis
"""


from rich import print
from utils_adso import texto_es_num_int, create_tabla


def numero_a_palabras(numero: int):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    especiales_10_19 = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete",
                        "dieciocho", "diecinueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

    if 0 <= numero <= 9:
        return unidades[numero]
    elif 10 <= numero <= 19:
        return especiales_10_19[numero - 10]
    elif 20 <= numero <= 99:
        return decenas[numero // 10] + (" y " + unidades[numero % 10] if numero % 10 != 0 else "")


def ej15():
    while True:
        create_tabla(titulo="Mostrar Forma Escrita de un Numero")
        print("  [bold cyan]Ingrese un numero entre el 0 y 99: ", end="")
        numero = texto_es_num_int(input())

        print(f"\n   [bold green]El numero {numero} es: {numero_a_palabras(numero)}\n\n" if 0 <= numero <= 99
              else "\n   [b yellow]El numero ingresado está fuera del rango permitido\n\n")
        print("[yellow]Presione una tecla para volver al menú...")
        return input()
