# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir dos cosas, la cantidad sin IVA y el porcentaje de IVA a 
# aplicar, y devolver el total de la factura. 
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 16%

def fac_iva(sin_iva, iva = 16): #sin_iva --> la cantidad sin IVA        iva -->porcentaje de IVA
    return sin_iva + sin_iva*iva/100

print(fac_iva(1600, 8))
print(fac_iva(1600))
