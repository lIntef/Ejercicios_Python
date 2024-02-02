import U1E01_Cociente
import U1E02_ParImpar
import U1E03_AreaCirculo
import U1E04_Multiplo2y3
import U1E05_IngresarFecha
import U1E06_MayorMenorMedio
import U1E07_HipotenuesaTriangulo
import U1E08_FechaCorrecta
import U1E09_TextoNumero
import U1E10_SegundosAHoras
import U1E11_NumerosInverso
import U1E12_CadenaPalindroma
import U1E13_OcurrenciasEnCadena
import U1E14_CaracteresPalindroma
import U1E15_NumeroATexto
import U1E16_CapitalizarFrase
import os
from rich import print
from rich import box
from rich.table import Table
from utils_adso import texto_es_num_int


def menu():
    table = Table(show_header=True, header_style="blue")
    table.title = (
        "\n\n[magenta]Bienvenido al desarrollo de lógica con Python\n"
        "[magenta]Edwin Alexander Correa Aullon\n"
        "[magenta]2670142\n"
    )
    table.add_column("Menu Principal", justify="center")
    table.add_row("[bold cyan]1..................................................Hallar Cociente")
    table.add_row("[bold cyan]2...............................................Hallar Par o Impar")
    table.add_row("[bold cyan]3...........................................Hallar Area de Circulo")
    table.add_row("[bold cyan]4...........................................Multiplo de Dos y Tres")
    table.add_row("[bold cyan]5.................................................Ingreso de Fecha")
    table.add_row("[bold cyan]6..........................Indicar Numero Mayor, del Medio y Menor")
    table.add_row("[bold cyan]7...................................Hallar Hipotenusa de Triangulo")
    table.add_row("[bold cyan]8.................Verificar Si el Ingreso de una Fecha es Correcta")
    table.add_row("[bold cyan]9.................Imprimir el Mes en Texto del Numero Seleccionado")
    table.add_row("[bold cyan]10.........Convertir Segundos Totales en Horas, Minutos y Segundos")
    table.add_row("[bold cyan]11................................Mostrar Numeros en Orden Inverso")
    table.add_row("[bold cyan]12..........................Determinar Si una Cadena es Palíndroma")
    table.add_row("[bold cyan]13.......Hallar Numero de Ocurrencias de un Caracter en una Cadena")
    table.add_row("[bold cyan]14................Determinar Si Cadena de Caracteres es Palíndroma")
    table.add_row("[bold cyan]15..............................Mostrar Forma Escrita de un Numero")
    table.add_row("[bold cyan]16.Solicitar una Frase Mínimo de 5 Palabras y Capitaliza la Cadena")
    table.add_row("[bold cyan]0............................................................SALIR")
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


if __name__ == '__main__':
    while True:
        os.system("cls")
        menu()
        print("\n[purple]Ingrese la opción que desea escoger: ", end="")
        op = input()
        op = texto_es_num_int(op)
        if op == 1:
            U1E01_Cociente.ej01()
        elif op == 2:
            U1E02_ParImpar.ej02()
        elif op == 3:
            U1E03_AreaCirculo.ej03()
        elif op == 4:
            U1E04_Multiplo2y3.ej04()
        elif op == 5:
            U1E05_IngresarFecha.ej05()
        elif op == 6:
            U1E06_MayorMenorMedio.ej06()
        elif op == 7:
            U1E07_HipotenuesaTriangulo.ej07()
        elif op == 8:
            U1E08_FechaCorrecta.ej08()
        elif op == 9:
            U1E09_TextoNumero.ej09()
        elif op == 10:
            U1E10_SegundosAHoras.ej10()
        elif op == 11:
            U1E11_NumerosInverso.ej11()
        elif op == 12:
            U1E12_CadenaPalindroma.ej12()
        elif op == 13:
            U1E13_OcurrenciasEnCadena.ej13()
        elif op == 14:
            U1E14_CaracteresPalindroma.ej14()
        elif op == 15:
            U1E15_NumeroATexto.ej15()
        elif op == 16:
            U1E16_CapitalizarFrase.ej16()
        elif op == 0:
            print("\n\n    [italic][b purple]Hasta Luego[/italic] 😀\n\n")
            exit(0)
