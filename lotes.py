from validaciones import validar_no_vacio, validar_numero_positivo, validar_codigo_unico

bd_lotes = {}

def registrar_lote(codigo, urbanizacion, area, precio_m2):
    codigo = validar_no_vacio(codigo, "Código")
    validar_codigo_unico(codigo, bd_lotes)
    urbanizacion = validar_no_vacio(urbanizacion, "Urbanización")
    area = validar_numero_positivo(area, "Área")
    precio_m2 = validar_numero_positivo(precio_m2, "Precio/m2")
    
    bd_lotes[codigo] = {
        "urbanizacion": urbanizacion,
        "area": area,
        "precio_m2": precio_m2,
        "estado": "Disponible"
    }
    return True

def listar_lotes():
    return bd_lotes

def obtener_lote(codigo):
    return bd_lotes.get(codigo)

def marcar_como_vendido(codigo):
    if codigo in bd_lotes and bd_lotes[codigo]["estado"] == "Disponible":
        bd_lotes[codigo]["estado"] = "Vendido"
        return True
    return False