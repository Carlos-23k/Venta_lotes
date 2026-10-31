from validaciones import validar_texto, validar_numero_positivo

# Base de datos en memoria para los lotes
db_lotes = []

def registrar_lote(codigo, urbanizacion, area, precio_m2):
    # Validar código único
    if any(lote['codigo'] == codigo for lote in db_lotes):
        return False, "Error: El código de lote ya se encuentra registrado."
    
    nuevo_lote = {
        'codigo': codigo,
        'urbanizacion': urbanizacion,
        'area': area,
        'precio_m2': precio_m2,
        'estado': 'Disponible'
    }
    db_lotes.append(nuevo_lote)
    return True, "Lote registrado con éxito."

def listar_disponibles():
    return [lote for lote in db_lotes if lote['estado'] == 'Disponible']

def obtener_lote(codigo):
    for lote in db_lotes:
        if lote['codigo'] == codigo:
            return lote
    return None

def marcar_como_vendido(codigo):
    lote = obtener_lote(codigo)
    if lote and lote['estado'] == 'Disponible':
        lote['estado'] = 'Vendido'
        return True
    return False
