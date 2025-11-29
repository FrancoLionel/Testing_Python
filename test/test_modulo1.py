import unittest

from modulo1.funciones import esPalindromo

class TestEsPalindromo(unittest.TestCase):
    def test_con_numeros(self):
        self.assertTrue(esPalindromo("99899"))
        self.assertFalse(esPalindromo("56789"))
    
    def test_espacio_signos(self):
        self.assertTrue(esPalindromo("l@a r*ut@a n#atúural"))
        self.assertTrue(esPalindromo("m @ a d # a # m"))
        

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