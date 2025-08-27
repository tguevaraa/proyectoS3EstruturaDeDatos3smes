def calcular(data):
  
    TASA_DESCUENTO = 0.15
    BASE_HORAS = 40
    TASA_HORA_EXTRA = 1.5
    BONO_EDAD = 40
    
    for empleado in data['empleados']:
        pago_por_hora = float(empleado.get('pagoPorHora', 0))
        horas_trabajadas = float(empleado.get('horasTrabajadas', 0))
        edad = int(empleado.get('edad', 0))

        if horas_trabajadas <= BASE_HORAS:
            pago_bruto = pago_por_hora * horas_trabajadas
        else:
            pago_base = pago_por_hora * BASE_HORAS
            horas_extras_trabajadas = horas_trabajadas - BASE_HORAS
            pago_extra = pago_por_hora * TASA_HORA_EXTRA * horas_extras_trabajadas
            pago_bruto = pago_base + pago_extra


        descuento = pago_bruto * TASA_DESCUENTO

        pago_neto = pago_bruto - descuento

        if edad >= 45:
            pago_neto += BONO_EDAD
            empleado['bono'] = BONO_EDAD
        else:
            empleado['bono'] = 0

        empleado['pagoBruto'] = round(pago_bruto, 2)
        empleado['descuento'] = round(descuento, 2)
        empleado['pagoNeto'] = round(pago_neto, 2)
        
    return data