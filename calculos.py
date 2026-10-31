def calcular_precios(area, precio_m2):
    precio_total = area * precio_m2
    cuota_inicial = precio_total * 0.20
    saldo = precio_total - cuota_inicial
    return precio_total, cuota_inicial, saldo