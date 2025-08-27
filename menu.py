import json
import os

import agregarEmpleado
import imprimirListaEmpleados
import calcularSalarios

dataBaseFile='dataBase.json'

def leerDatos(nombre_archivo):
    if not os.path.exists(nombre_archivo) or os.stat(nombre_archivo).st_size == 0:
        return {"empleados": []}
    with open(nombre_archivo, 'r') as archivo:
        return json.load(archivo)

def guardarDatos(datos, nombre_archivo):   
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print("Datos guardados exitosamente.")


def main():

    dataBase = leerDatos(dataBaseFile)    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar nuevo empleado")
        print("2. Calcular salarios")
        print("3. Ver lista de empleados")
        print("4. Guardar y salir")
        
        opcion=str(input("Selecione una opcion"))

        match opcion:
            case '1':
                dataBase = agregarEmpleado.agregar(dataBase)
                print("¡Empleado agregado exitosamente!") 
            case '2':
                dataBase = calcularSalarios.calcular(dataBase)
                print("Salarios calculados y actualizados para todos los empleados.")
            case '3':
                imprimirListaEmpleados.imprimirListaEmpleados(dataBase)
            case '4':
                guardarDatos(dataBase, dataBaseFile)
                print('¡Adiós!')
                break
            case _:
                print('Opción no válida, por favor ingrese una nueva opción.')

if __name__ == "__main__":
    main()