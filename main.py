import numpy as np
def menu():
    print("*****Bienvenido*****")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Decimal a Hexadecimal")
    opc = input("Digite una Opcion:\n")
    return opc


def decimalAHexadecimal():
    decimal = int(input("Ingrese el decimal a convertir:\n"))
    hexa = []
    resultado = ""
    while decimal >= 1:
        residuo = decimal % 16
        hexa.append(residuo)
        decimal = int(decimal / 16)
    impresionHexa = hexa[::-1]
    for i in impresionHexa:
        i = str(i)
        if i == "10":
            resultado = resultado + "A"
            continue
        elif i == "11":
            resultado = resultado + "B"
            continue
        elif i == "12":
            resultado = resultado + "C"
            continue
        elif i == "13":
            resultado = resultado + "D"
            continue
        elif i == "14":
            resultado = resultado + "E"
            continue
        elif i == "15":
            resultado = resultado + "F"
            continue
        else:
            resultado = resultado + i
    print(resultado)


def binarioADecimal():
    decimal = 0
    cont = 0
    binario = input("Digite su numero binario:\n")
    invertidoBinario = binario[::-1]
    for i in invertidoBinario:
        if i == "1":
            decimal += 2**cont
            cont += 1
        elif i == "0":
            cont += 1
            continue
    print("su numero en decimal es:\n" + str(decimal))


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
    print("Su numero binario es:\n "+ vlr)


def run():
    opcion = menu()
    if opcion == "1":
        decimalABinario()
    elif opcion == "2":
        binarioADecimal()
    elif opcion == "3":
        decimalAHexadecimal()


if __name__ == '__main__':
    run()