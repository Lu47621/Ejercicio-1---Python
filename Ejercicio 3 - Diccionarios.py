#Ejercicio 3. Diccionarios
#Escribir un programa que guarde en un diccionario los precios de las verduras de la tabla,
#pregunte al usuario por una verdura, un número de kilos y muestre por pantalla el precio de ese
#número de kilos de verdura, por ejemplo, 3.0 kilos de Brocoli valen $ 25.65. Si la verdura no 
#está en el diccionario debe mostrar un mensaje informando de ello.

#Verdura          Precio(kg)
#Brocoli             8.55
#Pepino              6.87
#Calabaza            11.55
#Chayote             14.33

print("----- Verduras disponibles -----")
print(" Verdura           Precio(kg)\n")
print(" Brocoli              8.55")
print(" Pepino               6.87")
print(" Calabaza             11.55")
print(" Chayote              14.33")
print("---------------------------------\n")

verduras = {"Brocoli":8.55, "Pepino":6.87, "Calabaza":11.55, "Chayote":14.33}
verd = input("¿Qué verdura quiere comprar? ").title() #title -> la primera letra mayuscula
kg = float(input("¿Cuántos kilos de dicha verdura desea? "))
if verd in verduras:
    print(f"{kg} kilos de {verd} valen ${verduras[verd]*kg:.2f}")
else: 
    print(f"La verdura {verd} no está disponible, disculpe las molestias.")
