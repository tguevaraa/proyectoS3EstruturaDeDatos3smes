import json
import os
def imprimirListaEmpleados(dataBase):
    
    empleados=dataBase['empleados']

    if not empleados:
        print("No hay empleados registrados para mostrar.")
        return

    for empleado in empleados:
        print(" ")
        for clave, valor in empleado.items():
            print(f"{clave}:  {valor}")


