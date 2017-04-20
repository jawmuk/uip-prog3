import unittest
from app.claseimparypar import Impar

class ParImparTestClase(unittest.TestCase):
    def setUp(self):
     self.numero = Impar(22)

    def test_Par(self):
      self.assertFalse(self.numero.num_par())

