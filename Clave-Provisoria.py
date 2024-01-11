#Hacer un programa que genere la clave provisoria para la gestión online de clientes de una
#empresa.
#El programa pedirá dos cadenas, nombre y apellido y tomará las 2 primeras consonantes de cada
#una de las palabras ingresadas. Cuando las consonantes no alcancen a 2 por palabra, las
#reemplazará por “_”.
#Ejemplos: Rosalía Pérez RSPR
#Eva Rodríguez V_RD
#Lea Oreo L_R_
#La clave se completará con 2 dígitos generados aleatoriamente entre 0 y 9. Y no se permite que la
#clave contenga números repetidos.
#Ejemplos: RSPR20
#V_RD45
#L_R_71

nombre=input("por favor, ingrese su nombre: ")
apellido=input("por favor, ingrese su apellido: ")
consonantes="bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
con_nombre=""
con_apellido=""
clave=""

c=1
for char in nombre:
    if char in consonantes:
        if c<=2:
            con_nombre+=char
        c+=1

while len(con_nombre)<2:  #si las consonantes no llegan a dos, agrega un guión bajo.
    con_nombre+="_"

c=1
for letra in apellido:
    if letra in consonantes:
        if c<=2:
            con_apellido+=letra
        c+=1

while len(con_apellido)<2:
    con_apellido+="_"