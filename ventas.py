from lotes import obtener_lote, marcar_como_vendido
from calculos import calcular_precios
from validaciones import validar_no_vacio

bd_ventas = []

def registrar_venta(codigo_lote, nombre_comprador, documento):
    lote = obtener_lote(codigo_lote)
    
    if not lote:
        raise ValueError("El lote no existe.")
    if lote["estado"] != "Disponible":
        raise ValueError("El lote ya se encuentra vendido o no está disponible.")
        
    nombre_comprador = validar_no_vacio(nombre_comprador, "Nombre Comprador")
    documento = validar_no_vacio(documento, "Documento")
    
    if marcar_como_vendido(codigo_lote):
        total, cuota, saldo = calcular_precios(lote["area"], lote["precio_m2"])
        
        venta = {
            "lote": codigo_lote,
            "comprador": nombre_comprador,
            "documento": documento,
            "precio_total": total,
            "cuota_inicial": cuota,
            "saldo": saldo
        }
        bd_ventas.append(venta)
        return venta
    else:
        raise ValueError("Error al actualizar el estado del lote.")

def listar_ventas():
    return bd_ventas