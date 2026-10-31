def validar_no_vacio(texto, campo):
    if not texto.strip():
        raise ValueError(f"El campo '{campo}' no puede estar vacío.")
    return texto.strip()

def validar_numero_positivo(valor, campo):
    try:
        numero = float(valor)
        if numero <= 0:
            raise ValueError(f"El campo '{campo}' debe ser mayor que cero.")
        return numero
    except ValueError:
        raise ValueError(f"El campo '{campo}' debe ser un número válido.")

def validar_codigo_unico(codigo, bd_lotes):
    if codigo in bd_lotes:
        raise ValueError(f"El código '{codigo}' ya existe.")
    return codigo