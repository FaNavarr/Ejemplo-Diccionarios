persona = {
    "rut": 211884431,
    "apellido":"pedro",
    "edad": 24,
    "altura":173,
    "lentes": True,
}


print(persona)#mala practica
print(persona["rut"])
print(persona["altura"])

#vamos a ver como recorrer un diccionario
for x in persona:
    print(x," - ",persona[x])


print( persona.keys() ) # muestra las llaves
print( persona.values() ) # muestra los valores
print( persona.items() )




print(persona)
persona["mascota"]= "Cholito" #si la llave no existe, la agrega
persona["edad"]= 26 #si la llave existe, modifica el valor!
persona.pop("altura") #al indicar la llave, se elimina la llave y el valor
print(persona)
print(persona.get)