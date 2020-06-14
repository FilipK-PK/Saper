''' klasa testujaca, moga pojawic sie komunikaty o bledzie 
	ktore wywoluje funkcja nie testujaca'''
import unittest
import okno_start


class OknoStartTest(unittest.TestCase):
    def testy_pobrane_zmiene(self):
        self.assertTrue(okno_start.testy_pobrane_zmiene(
            okno_start, '2', '2', '1'))
        self.assertFalse(okno_start.testy_pobrane_zmiene(
            okno_start, '2', '2', '2'))
        self.assertFalse(okno_start.testy_pobrane_zmiene(
            okno_start, '1', '2', '1'))

        self.assertTrue(okno_start.testy_pobrane_zmiene(
            okno_start, '15', '15', '75'))
        self.assertFalse(okno_start.testy_pobrane_zmiene(
            okno_start, '15', '16', '15'))
        self.assertFalse(okno_start.testy_pobrane_zmiene(
            okno_start, '15', '15', '76'))

        self.assertFalse(okno_start.testy_pobrane_zmiene(
            okno_start, 'a', '6', '3'))
        self.assertFalse(okno_start.testy_pobrane_zmiene(
            okno_start, '5', 'b', '2'))
        self.assertFalse(okno_start.testy_pobrane_zmiene(
            okno_start, '5', 'b', '0'))
        self.assertFalse(okno_start.testy_pobrane_zmiene(
            okno_start, '', 'b', '2'))
        self.assertFalse(okno_start.testy_pobrane_zmiene(
            okno_start, '-99', 'b', '0'))

        self.assertTrue(okno_start.testy_pobrane_zmiene(
            okno_start, '5', '5', '2'))
        self.assertTrue(okno_start.testy_pobrane_zmiene(
            okno_start, '14', '3', '10'))

if __name__ == '__main__':
    unittest.main()
