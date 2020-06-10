''' klasa testujaca, moga pojawic sie komunikaty o bledzie 
	ktore wywoluje funkcja nie testujaca'''
import unittest
from okno_start import OknoStart


class OknoStartTest(unittest.TestCase):
    def testy_pobrane_zmiene(self):
        self.assertTrue(OknoStart.testy_pobrane_zmiene(
            OknoStart, '2', '2', '1'))
        self.assertFalse(OknoStart.testy_pobrane_zmiene(
            OknoStart, '2', '2', '2'))
        self.assertFalse(OknoStart.testy_pobrane_zmiene(
            OknoStart, '1', '2', '1'))

        self.assertTrue(OknoStart.testy_pobrane_zmiene(
            OknoStart, '15', '15', '75'))
        self.assertFalse(OknoStart.testy_pobrane_zmiene(
            OknoStart, '15', '16', '15'))
        self.assertFalse(OknoStart.testy_pobrane_zmiene(
            OknoStart, '15', '15', '76'))

        self.assertFalse(OknoStart.testy_pobrane_zmiene(
            OknoStart, 'a', '6', '3'))
        self.assertFalse(OknoStart.testy_pobrane_zmiene(
            OknoStart, '5', 'b', '2'))
        self.assertFalse(OknoStart.testy_pobrane_zmiene(
            OknoStart, '5', 'b', '0'))
        self.assertFalse(OknoStart.testy_pobrane_zmiene(
            OknoStart, '', 'b', '2'))
        self.assertFalse(OknoStart.testy_pobrane_zmiene(
            OknoStart, '-99', 'b', '0'))

        self.assertTrue(OknoStart.testy_pobrane_zmiene(
            OknoStart, '5', '5', '2'))
        self.assertTrue(OknoStart.testy_pobrane_zmiene(
            OknoStart, '14', '3', '10'))

if __name__ == '__main__':
    unittest.main()
