#Ejercicio 5 - Reloj
import os
import time

while True:
    try:
        entrada = input("Ingrese la hora, Hora:Minutos:Segundos de esta manera: ")
        lista = entrada.split(":") ## 5:12:41 - ["5", "12", "41"]
        e_hora = int(lista [0])
        e_minuto = int(lista[1])
        e_segundo = int(lista[2])
        if e_hora >= 0 and e_hora <= 23:
            if e_minuto >= 0 and e_minuto <= 59:
                if e_segundo >= 0 and e_segundo <= 59:
                    print(lista)

                    for hora in range(e_hora, 24):
                        for minuto in range(e_minuto, 60):
                            for segundo in range(e_segundo, 60):
                                os.system("cls")
                                print(f"{hora}:{minuto}:{segundo}")
                                time.sleep(1)
                                    
                                if segundo == 59:
                                    segundo = 0
                                    e_segundo = 0
                                
                            if minuto == 59:
                                minuto = 0
                                e_minuto = 0 
                                
                        if hora == 23:
                            hora = 0
                            e_hora = 0
        else:
            print("Error... No estas dentro del rango de la hora real [0 - 23 horas, ejemplo: 00:05:45]")
    except ValueError:
        print("Hora introducida no valida. Debe de ser de la siguiente manera \nHora:Minutos:Segundos (Ejemplo: 17:05:12) \n\n")
