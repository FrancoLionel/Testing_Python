import unicodedata
import unittest

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

class TestEsPalindromo(unittest.TestCase):
    def test_con_numeros(self):
        self.assertTrue(esPalindromo("99899"))
        self.assertFalse(esPalindromo("56789"))
    
    def test_espacio_signos(self):
        self.assertTrue(esPalindromo("l@a r*ut@a n#atural"))
        self.assertTrue(esPalindromo("m @ a d # a # m"))
        
    def test_cadena_vacía(self):
        self.assertTrue(esPalindromo(""))

    def test_solo_espacios(self):
        self.assertTrue(esPalindromo("     "))

    def test__solo_caracter(self):
        self.assertTrue(esPalindromo("a"))
        self.assertTrue(esPalindromo("1"))

    def test_con_tildes(self):
        self.assertTrue(esPalindromo("Ánita láva la tina"))
        self.assertTrue(esPalindromo("A mamá Roma le aviva el amor a mamá"))

    def test_enie(self):
        self.assertTrue(esPalindromo("Añá"))    

    def test_palindromo_largo(self):
        cadena = "a" * 1000000
        self.assertTrue(esPalindromo(cadena)) 

    def test_palindromo_correcto(self):
        self.assertTrue(esPalindromo("reconocer"))
        self.assertTrue(esPalindromo("salas"))
        self.assertTrue(esPalindromo("salas"))
        self.assertTrue(esPalindromo("madam"))
    
    def test_palindromo_mayus_espacio(self):
        self.assertTrue(esPalindromo("La Ruta Natural"))
        self.assertTrue(esPalindromo("A Ti No Bonita"))
    

if __name__ == "__main__":
    unittest.main()

