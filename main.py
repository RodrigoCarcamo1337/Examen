import funciones as FuncionMaestra

trabajadores = ["Juan Perez","Maria Garcia","Carlos López","Ana Martinez","Pedro Rodriguez","Laura Hernandez", "Miguel Sanchez", "Isabel Gomez","Francisco Diaz","Helena Fernandez"]


while True:

    try:
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")


        opc = int(input("Ingrese una opcion: "))

        if opc == 1:
            FuncionMaestra.Asignar_sueldos()
            print("----------------------------------")
        elif opc == 2:
            FuncionMaestra.Clasificar_sueldos()
            print("----------------------------------")
        elif opc == 3:
            FuncionMaestra.Estadisticas()
            print("----------------------------------")
        elif opc == 4:
            FuncionMaestra.ReporteSueldos()
            print("----------------------------------")
        
        elif opc == 5:
            print("Finalizando Programa...")
            print("Desarrollado por Rodrigo Cárcamo")
            print("RUT 21.327.289-6")
            break

    except ValueError:
        print("Ingrese un valor valido")
        print("----------------------------------")