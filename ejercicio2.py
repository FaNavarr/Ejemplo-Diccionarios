notas = {
    "Pedro": 5.5,
    "María": 6.2,
    "Juan": 4.8,
    "Ana": 7.0
}

nombre = input("Ingrese nombre de usuario: ")

if nombre in notas:
    print("La nota de", nombre, "es", notas[nombre])
else:
    print("El nombre no existe")