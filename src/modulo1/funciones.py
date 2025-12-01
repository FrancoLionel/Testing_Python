import unicodedata

def quitar_acento_tildes(cadena):
  
    cadena = unicodedata.normalize("NFD", cadena)
    return ''.join(c for c in cadena if unicodedata.category(c) != "Mn")

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas y tildes.
    """

    if not isinstance(cadena, str):
        raise TypeError("La cadena debe ser un string")
    
    # Normalizar (quita tildes y acentos)
    cadena = quitar_acento_tildes(cadena)

    # Convertir la cadena a minúsculas y eliminar caracteres no alfanuméricos
    cadena_limpia = ''.join(char.lower() for char in cadena if char.isalnum())

    # Comparar la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]
