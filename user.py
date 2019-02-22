# PROGRAMA QUE REVISA EL USUARIO INTRODUCIDO MEDIANTE EXPRESIONES REGULARES

import re

def comprobarUsuario (usuario):
    patron =  re.compile('\D[\w][\d]?')
    resultado = patron.match(usuario)

    if str(resultado) == "None":
        print("El usuario no es correcto")
    else:
        print("El usuario introducido es correcto")

usuario = input("Introduce un nombre de usuario para comprobar: ")

comprobarUsuario(usuario)


    
