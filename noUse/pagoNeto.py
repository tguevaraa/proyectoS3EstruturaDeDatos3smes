import json
def pagoNeto(dataBase):
    with open('dataBase.json','r') as archivo:
        dataBase=json.load(archivo)
    bono=40
    for empleado in dataBase['empleados']:
        pagoBruto= float(empleado['pagoBruto'])
        taxes=float(empleado['descuento'])
        edad=int(empleado['edad'])
        

        if edad >=45:    
            pagoNeto=pagoBruto-taxes+bono
            empleado['bono']=True
        else:
            pagoNeto=pagoBruto-taxes
            empleado['bono']=False
        print(f"el sueldo a pagar del/la sr/a. {empleado['nombre']} {empleado['apellido']}")
        print(f"es de: ${pagoNeto:.2f}")
        empleado['pagoNeto']=round(pagoNeto,2)

    return dataBase
try:
    with open('dataBase.json','r') as archivo:
        dataBase= json.load(archivo)
except(FileNotFoundError, json.JSONDecodeError):
    print("Archivo 'dataBase.json' no encontrado o vacío. Creando uno nuevo.")
    dataBase = {"empleados": []}

pagoNetoActualizado=pagoNeto(dataBase)

with open('dataBase.json', 'w') as archivo:
    json.dump(dataBase, archivo, indent=4)   