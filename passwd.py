import re

def validarContraseña (contraseña):
    patron = re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-.]).{8,16}$")
    resultado = patron.match(contraseña)

    if str(resultado) == "None":
        print("La contraseña no es fuerte")
    else:
        print("La contraseña es fuerte")

contraseña = input("Introduce una contraseña para comprobar su fortaleza: ")

validarContraseña(contraseña)