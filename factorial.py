# EJERCICIO QUE DEVUELVE FACTORIAL DE UN NUMERO

def factorial(x,n):
	
	if(n>0):
		x=factorial(x, n-1)
		x=x*n
	else:
		x=1
	return x
 
try:
	numero = int(input("Inserta un numero "))
 
	calculo=factorial(1,numero)
	print("El factorial de ", numero, " es ", calculo)
except:
	print("Tiene que ser un valor numerico")