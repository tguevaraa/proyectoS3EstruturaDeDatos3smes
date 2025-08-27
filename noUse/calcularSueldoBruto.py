import json
def calcularSueldoBruto(dataBase):    
    with open('dataBase.json','r') as archivo:
        dataBase=json.load(archivo)


    for empleado in dataBase['empleados']:
        edad = int(empleado['edad'])
        pago_por_hora = float(empleado['pagoPorHora'])
        horas_trabajadas = float(empleado['horasTrabajadas'])
        base_horas= 40
        horas_extras=1.5
        
        if horas_trabajadas <= base_horas:
            pago_bruto = pago_por_hora * horas_trabajadas
        elif horas_trabajadas > base_horas:
            pago_bruto= pago_por_hora*base_horas + pago_por_hora * horas_extras*(horas_trabajadas-base_horas)
        
        print(f"El Sr(a). {empleado['nombre']} {empleado['apellido']} ({edad} años) ganó: ${pago_bruto:.2f}")

        empleado['pagoBruto'] = round(pago_bruto,2)
    return dataBase


try:
    with open('dataBase.json','r') as archivo:
        dataBase= json.load(archivo)
except(FileNotFoundError, json.JSONDecodeError):
    print("Archivo 'dataBase.json' no encontrado o vacío. Creando uno nuevo.")
    dataBase = {"empleados": []}

dataBaseActualizada=calcularSueldoBruto(dataBase)

with open('dataBase.json', 'w') as archivo:
    json.dump(dataBase, archivo, indent=4)
    print("\nCambios guardados exitosamente en 'dataBase.json'.")