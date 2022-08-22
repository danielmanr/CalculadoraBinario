import numpy as np
def menu():
    print("*****Bienvenido*****")
    print("Digite una Opcion para la Unidad de Entrada:\n")
    print("1. Decimal")
    print("2. Binario")
    print("3. Hexadecimal")
    print("4. Octal")
    print("5. Salir")
    opc = input()
    return opc

def decimalAOctal(decimal):
    oct = []
    while decimal > 0:
        residuo = int(decimal % 8)
        oct.append(residuo)
        decimal = int(decimal / 8)
    impresionOctal = oct[::-1]
    vlr = ""
    for i in impresionOctal:
        istring = str(i)
        vlr += istring
    vlr = int(vlr)
    return vlr



def decimalAHexadecimal(decimal):
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
    return resultado


def binarioADecimal(binario):
    decimal = 0
    cont = 0
    invertidoBinario = binario[::-1]
    for i in invertidoBinario:
        if i == "1":
            decimal += 2**cont
            cont += 1
        elif i == "0":
            cont += 1
            continue
    return decimal


def decimalABinario(decimal):
    bina = []
    while decimal >= 1:
        if decimal % 2 == 0:
            bina.append("0")
            decimal = int(decimal / 2)
        else:
            bina.append("1")
            decimal = int(decimal / 2)
    impresionBinario = bina[::-1]
    vlr = ""
    for i in impresionBinario:
        vlr += i
    vlr = int(vlr)
    return vlr


def run():
    opcion = menu()
    if opcion == "1":
        decimal = int(input("Digite el Valor Decimal: \n"))
        binario = decimalABinario(decimal)
        hexadecimal = decimalAHexadecimal(decimal)
        octal = decimalAOctal(decimal)
        print("Su valor en Binario es: " + str(binario) + "\n")
        print("Su Valor en Hexadecimal es: " + str(hexadecimal) + "\n")
        print("Su Valor en Octal es : " + str(octal) + "\n")
    elif opcion == "2":
        binario = input("Digite el Valor Binario: \n")
        decimal = binarioADecimal(binario)
        hexadecimal = decimalAHexadecimal(decimal)
        octal = decimalAOctal(decimal)
        print("Su Valor en Decimal es : " + str(decimal) + "\n")
        print("Su Valor en Hexadecimal es: " + hexadecimal + "\n")
        print("Su Valor en Octal es : " + str(octal) + "\n")

    elif opcion == "3":
        decimalAHexadecimal()


if __name__ == '__main__':
    run()