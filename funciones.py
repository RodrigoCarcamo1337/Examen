import random
import statistics
import csv
trabajadores = ["Juan Perez","Maria Garcia","Carlos López","Ana Martinez","Pedro Rodriguez","Laura Hernandez", "Miguel Sanchez", "Isabel Gomez","Francisco Diaz","Helena Fernandez"]

Lista = []
def Asignar_sueldos():
    for trabajador in trabajadores:
        Sueldo = random.randint(300000,2500000)

        Lista.append({"Nombre": trabajador, 
                      "Sueldo": Sueldo
                      })
    print("Creditos asignados")
    return Lista


def Clasificar_sueldos():
    lista_sueldo_pequeno = []
    lista_sueldo_medio = []
    lista_sueldo_alto = []

    for trabajador in Lista:
        if trabajador["Sueldo"] < 800000:
            lista_sueldo_pequeno.append(trabajador)
        elif trabajador["Sueldo"] >= 800000 and trabajador["Sueldo"] <= 2000000:
            lista_sueldo_medio.append(trabajador)
        else:
            lista_sueldo_alto.append(trabajador)

    print("Sueldos menos a $800.000")
    print("total de sueldos:" + str(len(lista_sueldo_pequeno)))
    print("Nombre Empleado  Sueldo")
    for trabajador in lista_sueldo_pequeno:
        print(trabajador["Nombre"] + " " + str(trabajador["Sueldo"]))
    print("----------------------------------")

    print("Sueldos entre $800.000 y $2.000.000")
    print("total de sueldos:" + str(len(lista_sueldo_medio)))
    print("Nombre Empleado  Sueldo")
    for trabajador in lista_sueldo_medio:
        print(trabajador["Nombre"] + " " + str(trabajador["Sueldo"]))
    print("----------------------------------")

    print("Sueldos mayores a $2.000.000")
    print("total de sueldos:" + str(len(lista_sueldo_alto)))
    print("Nombre Empleado  Sueldo")
    for trabajador in lista_sueldo_alto:
        print(trabajador["Nombre"] + " " + str(trabajador["Sueldo"]))
    
    print("Total de sueldos: " + str(len(Lista)))

    return lista_sueldo_pequeno, lista_sueldo_medio, lista_sueldo_alto



def Estadisticas():
    sueldos = []
    sumaSueldos = 0
    Valor = 0
    for trabajador in Lista:
        sueldos.append(trabajador["Sueldo"])
    print("El sueldo más alto es: " + str(max(sueldos)))
    print("El sueldo más bajo es: " + str(min(sueldos)))

    for trabajador in Lista:
        sumaSueldos += trabajador["Sueldo"]
        Valor = Valor + 1
    promedio = sumaSueldos / Valor
    print("El sueldo promedio es: ", promedio)
    media = statistics.median(sueldos)
    print("La media geometrica es:", media)



def ReporteSueldos():
    print("Generando reporte de sueldos")
    with open("reporte.csv", "w", newline="") as archivo:
        clasificador = csv.writer(archivo)
        clasificador.writerow(["Nombre", "SueldoBase", "DescuentoSalud", "DescuentoAFP", "SueldoLiquido"])
        for trabajador in Lista:
            descuento_salud = trabajador["Sueldo"]*0.07
            descuento_afp = trabajador["Sueldo"]*0.12
            sueldo_liquido = trabajador["Sueldo"] - descuento_salud - descuento_afp
            clasificador.writerow([trabajador["Nombre"], trabajador["Sueldo"], descuento_salud, descuento_afp, sueldo_liquido])
    print("Reporte generado")