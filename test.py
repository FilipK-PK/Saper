''' klasa testujaca '''
import unittest
from okno_start import OknoStart


class OknoStartTest(unittest.TestCase):
    ''' testowanie  '''
    def pobrane_zmiene_test(self):
        ''' testowanie zmiennych pobranych z okna start'''
        # moga pojawic sie komunikaty o bledzie ktore wywoluje funkcja
        # nie testujaca
        self.assertTrue(OknoStart.pobrane_zmiene_test(
            OknoStart, '2', '2', '1'))
        self.assertFalse(OknoStart.pobrane_zmiene_test(
            OknoStart, '2', '2', '2'))
        self.assertFalse(OknoStart.pobrane_zmiene_test(
            OknoStart, '1', '2', '1'))

        self.assertTrue(OknoStart.pobrane_zmiene_test(
            OknoStart, '15', '15', '75'))
        self.assertFalse(OknoStart.pobrane_zmiene_test(
            OknoStart, '15', '16', '15'))
        self.assertFalse(OknoStart.pobrane_zmiene_test(
            OknoStart, '15', '15', '76'))

        self.assertFalse(OknoStart.pobrane_zmiene_test(
            OknoStart, 'a', '6', '3'))
        self.assertFalse(OknoStart.pobrane_zmiene_test(
            OknoStart, '5', 'b', '2'))
        self.assertFalse(OknoStart.pobrane_zmiene_test(
            OknoStart, '5', 'b', '0'))

        self.assertTrue(OknoStart.pobrane_zmiene_test(
            OknoStart, '5', '5', '2'))
        self.assertTrue(OknoStart.pobrane_zmiene_test(
            OknoStart, '14', '3', '10'))
