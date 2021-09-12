import unittest
from kata_file import *

class TestFuncion(unittest.TestCase):
    def test_funcion(self):
        self.assertEqual(funcion(1),2)
        self.assertEqual(funcion(3),6)
        self.assertEqual(funcion(5),10)
