from funciones import *

BD = [
    {
        "nombre": "Juanito",
        "apellido": "Perez",
        "sede": "cerrillos",
        "ID": 1,
        "asistencias": [{"fecha": "2024-07-01", "tiempo": 60}, {"fecha": "2024-07-03", "tiempo": 50}]
    }
]

print("¡Bienvenido al control de gestion de clientes FITNESS CLUB!")

while True:

    # LOS PRINTS DEL MENU 
    menu()

    # ELEGIR UNA OPCIÓN
    opcion = input("Ingrese la opción a ejecutar: ")

    if opcion == "1":
        registrar_socio(BD)

    elif opcion == "2":
        listar_clientes(BD)

    elif opcion == "3":
        registrar_asistencia(BD)

    elif opcion == "4":
        listar_asistencias(BD)

    elif opcion == "5":
        print("HASTA LA PRÓXIMA!")
        break 

    else:
        print("%$&$! HAGALO OTRA VEZ")

    








