agenda = {}
nombres = []
telefonos = []

#for x in range(3):
#    nombre = input(f"Ingrese nombre {x+1}: ")
#    telefono = int(input(f"Ingrese telefono {x+1}: "))
#
#    nombres.append(nombre)
#    telefonos.append(telefono)
#
#agenda["nombres"] = nombres
#agenda["telefonos"] = telefonos
#
#for clave, valor in agenda.items():
#    print(clave, "-", valor)



#ejercicio 1: forma 2:

agenda = []

for x in range(3):
    nombre = input(f"Ingrese nombre {x+1}: ")
    telefono = int(input(f"Ingrese telefono {x+1}: "))
    contacto = {
        "nombre": nombre,
        "telefono": telefono
    }
    agenda.append(contacto)

for x in agenda:
    print(x,["nombre"]," -> ", x["telefono"])