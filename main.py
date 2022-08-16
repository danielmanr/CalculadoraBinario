import numpy as np
def menu():
    print("*****Bienvenido*****")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    opc = input("Digite una Opcion:\n")
    return opc

def binarioADecimal():
    decimal = 0
    cont = 0
    binario = input("Digite su numero binario:\n")
    invertidoBinario = binario[::-1]
    for i in invertidoBinario:
        if i == "1":
            if cont >= 1:
                decimal += 2**cont
                cont += 1
                continue
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





if __name__ == '__main__':
    run()