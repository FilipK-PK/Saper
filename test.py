import unittest
from oknoStart import OknoStart


class Test_OknoStart(unittest.TestCase):
    def test_sprawdzanie_Wartosci_Poczatkowych(self):
        # moga pojawic sie komunikaty o błedzie które wywołuje funkcja nie testujaca
        self.assertTrue(OknoStart.sprawdzanie_Wartosci_Poczatkowych(OknoStart, '2', '2', '1'))
        self.assertFalse(OknoStart.sprawdzanie_Wartosci_Poczatkowych(OknoStart, '2', '2', '2'))
        self.assertFalse(OknoStart.sprawdzanie_Wartosci_Poczatkowych(OknoStart, '1', '2', '1'))

        self.assertTrue(OknoStart.sprawdzanie_Wartosci_Poczatkowych(OknoStart, '15', '15', '75'))
        self.assertFalse(OknoStart.sprawdzanie_Wartosci_Poczatkowych(OknoStart, '15', '16', '15'))
        self.assertFalse(OknoStart.sprawdzanie_Wartosci_Poczatkowych(OknoStart, '15', '15', '76'))

        self.assertFalse(OknoStart.sprawdzanie_Wartosci_Poczatkowych(OknoStart, 'a', '6', '3'))
        self.assertFalse(OknoStart.sprawdzanie_Wartosci_Poczatkowych(OknoStart, '5', 'b', '2'))
        self.assertFalse(OknoStart.sprawdzanie_Wartosci_Poczatkowych(OknoStart, '5', 'b', '0'))

        self.assertTrue(OknoStart.sprawdzanie_Wartosci_Poczatkowych(OknoStart, '5', '5', '2'))
        self.assertTrue(OknoStart.sprawdzanie_Wartosci_Poczatkowych(OknoStart, '14', '3', '10'))
