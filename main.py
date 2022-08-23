import numpy as np
def menuContinuacion():
    print("Desea seguir realizando conversiones: \n")
    print("1. Si")
    print("2. No")
    opc = input()
    if opc == "1":
        run()
    if opc == "2":
        quit()

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

def octalADecimal(octal):
    arrOctal = []
    count = 0
    decimal = 0
    for i in octal:
        arrOctal.append(int(i))
    inverOctal = arrOctal[::-1]

    for i in inverOctal:
        result = i *(8 ** count)
        decimal = decimal + result
        count += 1
    return decimal


def hexadecimalADecimal(hexa):
    arrHexa = []
    count = 0
    decimal = 0
    for i in hexa:
        arrHexa.append(i)
    inverHexa = arrHexa[::-1]

    for i in inverHexa:
        if i == "A":
            base = 10;
        elif i == "B":
            base = 11
        elif i == "C":
            base = 12
        elif i == "D":
            base = 13
        elif i == "E":
            base = 14
        elif i == "F":
            base = 15
        else:
            base = int(i)
        suma = base * (16**count)
        decimal = decimal + suma
        count += 1
    return decimal


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
        menuContinuacion()
    elif opcion == "2":
        binario = input("Digite el Valor Binario: \n")
        decimal = binarioADecimal(binario)
        hexadecimal = decimalAHexadecimal(decimal)
        octal = decimalAOctal(decimal)
        print("Su Valor en Decimal es : " + str(decimal) + "\n")
        print("Su Valor en Hexadecimal es: " + hexadecimal + "\n")
        print("Su Valor en Octal es : " + str(octal) + "\n")
        menuContinuacion()
    elif opcion == "3":
        hexa = input("Digite el Valor en Hexadecimal: \n")
        decimal = hexadecimalADecimal(hexa)
        binario = decimalABinario(decimal)
        octal = decimalAOctal(decimal)
        print("Su Valor en Binario es : " + str(binario) + "\n")
        print("Su Valor en Decimal es: " + str(decimal) + "\n")
        print("Su Valor en Octal es : " + str(octal) + "\n")
        menuContinuacion()
    elif opcion == "4":
        octal = input("Digite el Valor en Octal: \n")
        decimal = octalADecimal(octal)
        hexa = decimalAHexadecimal(decimal)
        binario = decimalABinario(decimal)
        print("Su Valor en Binario es : " + str(binario) + "\n")
        print("Su Valor en Decimal es: " + str(decimal) + "\n")
        print("Su Valor en Hexadecimal es : " + hexa + "\n")
        menuContinuacion()
    elif opcion == "5":
        quit()


if __name__ == '__main__':
    run()