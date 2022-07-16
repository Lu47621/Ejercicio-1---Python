##### Ejercicio 1 - Ficha de Datos #####
Nombre = input("Ingresa tu nombre: ") ##Entrada de datos por parte del usuario
N_telefono = input("Ingresa tu numero telefonico: ")
Direccion = input("Ingresa tu direccion: ")
Edad = input("Ingresa tu edad: ")
Nacionalidad = input("Ingresa tu nacionalidad: ")
Fecha_naci = input("Ingresa tu fecha de nacimiento: ")
Altura = input("Ingresa tu altura: ")
print(f"Ejemplo de Peso: 58.2 kg")
Peso = input("Ingresa tu peso: ")


print(f"\n Nombre: {Nombre}")
print(type(Nombre))##Muestra el tipo de entrada

print(f"Numero de telefono: {N_telefono}")
numero = int (N_telefono)
print(type(numero))##Muestra el tipo de entrada

print(f"Direccion: {Direccion}")
print(type(Direccion))##Muestra el tipo de entrada

print(f"Edad: {Edad} años")
e = int (Edad)
print(type(e))##Muestra el tipo de entrada

print(f"Nacionalidad: {Nacionalidad}")
print(type(Nacionalidad))##Muestra el tipo de entrada

print(f"Fecha de nacimiento: {Fecha_naci}")
print(type(Fecha_naci))##Muestra el tipo de entrada

print(f"Altura: {Altura} cm")
a = int (Altura)
print(type(a))##Muestra el tipo de entrada

print(f"Peso: {Peso} kg")
p = float(Peso)
print(type(p))##Muestra el tipo de entrada