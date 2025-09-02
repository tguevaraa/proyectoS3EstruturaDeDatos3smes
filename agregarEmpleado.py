import json    
def agregar(dataBase):
    nuevoEmpleado = {
        "id": int(input("Ingrese el ID del empleado: ")),
        "nombre": input("Ingrese su nombre: "),
        "apellido": input("Ingrese su apellido: "),
        "edad": int(input("Ingrese su edad: ")),
        "pagoPorHora": float(input("Ingrese cuanto cobra por hora: ")),
        "horasTrabajadas": int(input("Ingrese el total de horas trabajadas: "))
    }
    dataBase['empleados'].append(nuevoEmpleado)
    print("El empleado se agregó correctamente")
    return dataBase
        