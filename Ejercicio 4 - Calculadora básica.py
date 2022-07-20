#Ejercicio 4 - Calculadora básica
import os
#Listas
ns1=[] 
ns2=[]
nr1=[]
nr2=[]
nm1=[]
nm2=[]
nd1=[]
nd2=[]
rs=[]
rr=[]
rd=[]
rm=[]

print("------------------ Calculadora básica ------------------\n")
while True:
    
    decision = input("¿Desea realizar alguna operación? \n S = Si   N = No : ")
    if decision == 's' or decision == 'S':
        os.system("cls")
        print("------------------------- Menú -------------------------")
        print("1. Suma")
        print("2. Resta")
        print("3. Mulitplicación")
        print("4. División")
        print("5. Historial \n")
        opcion = input("\nIngrese la opcion a realizar: ")
        op = int(opcion)
        if op >=1 and op <=5:
            
            if op == 1:
                os.system("cls")
                print("---------- Suma ----------\n")
                n_1 = float(input("Ingresa el primer número: "))
                ns1.append(n_1)
                n_2 = float(input("Ingresa el segundo número: "))
                ns2.append(n_2)
                r_s = n_1 + n_2
                rs.append(r_s,)
                print(f"\nLa suma de  {n_1} + {n_2} = {r_s:.2f} \n\n")
                continue
                
            elif op == 2:
                os.system("cls") 
                print("---------- Resta ----------\n")
                n_1 = float(input("Ingresa el primer número: "))
                nr1.append(n_1)
                n_2 = float(input("Ingresa el segundo número: "))
                nr2.append(n_2)
                r_r = n_1 - n_2
                rr.append(r_r)
                print(f"\nLa resta de  {n_1} - {n_2} = {r_r:.2f}\n\n")
                continue

            elif op == 3:
                os.system("cls")
                print("---------- Multiplicación ----------\n")
                n_1 = float(input("Ingresa el primer número: "))
                nm1.append(n_1)
                n_2 = float(input("Ingresa el segundo número: "))
                nm2.append(n_2)
                r_m = n_1 * n_2
                rm.append(r_m)
                print(f"\nLa multiplicación de  {n_1} * {n_2} = {r_m:.2f}\n\n")
                continue

            elif op == 4:
                os.system("cls")
                print("---------- División ----------\n")
                n_1 = float(input("Ingresa el primer número: "))
                nd1.append(n_1)
                n_2 = float(input("Ingresa el segundo número: "))
                nd2.append(n_2)
                r_d = n_1 / n_2
                rd.append(r_d)
                print(f"\nLa división de  {n_1} / {n_2} = {r_d:.2f}\n\n")
                continue
            elif op == 5:
                os.system("cls")
                print("---------- Historial ----------")
                
                if len((ns1 and ns2) or (nr1 and nr2) or (nm1 and nm2) or (nd1 and nd2)) == 0:
                    print("\n      No hay historial\n\n")
                else:
                    
                    print(f"Suma: {ns1} + {ns2} = {rs}")     
                    print(f"Resta: {nr1} - {nr2} = {rr}")
                    print(f"Multiplicación: {nm1} * {nm2} = {rm}")
                    print(f"División: {nd1} / {nd2} = {rd} \n")
                    de = int(input("\n¿Desea eliminar el historial? \n1 = Si    2 = No : "))
                    if de == 1:
                        ns1.clear()
                        ns2.clear()
                        rs.clear()
                        nr1.clear()
                        nr2.clear()
                        rr.clear()
                        nm1.clear()
                        nm2.clear()
                        rm.clear()
                        nd1.clear()
                        nd2.clear()
                        rd.clear()
                        print("\nEl historial se ha eliminado correctamente\n\n")
                    elif de == 2:
                        continue
                    else: 
                        print("\nOpción invalida\n")
                        continue
            #break
        else:
            print("\nOpción invalida\n")
            
    else:
        exit()


