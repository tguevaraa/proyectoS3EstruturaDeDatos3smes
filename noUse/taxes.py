import json
def calcularTaxes(dataBase):
    with open('dataBase.json','r') as archivo:
        dataBase=json.load(archivo)

    for empleado in dataBase['empleados']:
        pagoBruto= float(empleado['pagoBruto'])
        tax=0.15
        taxes=pagoBruto*tax
        print(f"el descuento del sr/a {empleado['nombre']} sera de: ${taxes:.2f}")
        empleado['descuento']=round(taxes,2)
try:
    with open('dataBase.json','r') as archivo:
        dataBase= json.load(archivo)
except(FileNotFoundError, json.JSONDecodeError):
    print("Archivo 'dataBase.json' no encontrado o vacío. Creando uno nuevo.")
    dataBase = {"empleados": []}

taxesActualizados=calcularTaxes(dataBase)

with open('dataBase.json', 'w') as archivo:
    json.dump(dataBase, archivo, indent=4)