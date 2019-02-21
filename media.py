
# PROGRAMA PARA SACAR LA MEDIA DE VARIOS NUMEROS INTRODUCIDOS
numeroIntroducido = 0
cantidadNumeros = 0
sumaIntroducidos = 0
resultado = 0

fin = False

while fin != True:
    str(numeroIntroducido)
    numeroIntroducido = input("Introduce un numero: ")
    if str(numeroIntroducido) == "exit":
        resultado = sumaIntroducidos / cantidadNumeros
        fin = True
        print("La media es: ", resultado)
    else:
        float(numeroIntroducido)
        sumaIntroducidos = sumaIntroducidos + float(numeroIntroducido)
        cantidadNumeros =  cantidadNumeros + 1
       

