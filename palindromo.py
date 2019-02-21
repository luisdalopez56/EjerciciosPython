# COMPROBAR SI LA PALABRA ES PALINDROMA

palabraIntroducida = 'Ojol'

# CONVERTIMOS LAS LETRAS EN MINUSCULAS
palabraIntroducida = palabraIntroducida.casefold()

# INVIERTE LA PALABRA
rev_str = reversed(palabraIntroducida)

# COMPRUEBA SI LA PALABRA ES IGUAL DE FORMA NORMAL Y A LA INVERSA
if list(palabraIntroducida) == list(rev_str):
   print("Es palindroma")
else:
   print("No es palindroma")