import numpy as np
def menu():
    print("*****Bienvenido*****")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    opc = input("Digite una Opcion:\n")
    return opc


def decimalABinario():
    decimal = int(input("Ingrese el decimal a convertir:\n"))
    bina = []
    while decimal >= 1:
        if decimal % 2 == 0:
            bina.append("0")
            decimal = decimal / 2
        else:
            bina.append("1")
            decimal = decimal / 2

    impresionBinario = bina[::-1]
    vlr = ""
    for i in impresionBinario:
        vlr += i
    print("Su numero binario es: "+ vlr)





def run():
    opcion = menu()
    if opcion == "1":
        decimalABinario()





if __name__ == '__main__':
    run()