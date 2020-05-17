from logika import Logika
from grafika import Grafika

class Plansza(Logika, Grafika):
    def __init__(self, s, w, b):
        self.w = w
        self.s = s
        self.b = b
        self.liczbikB = self.b
        self.ox = int((600 - s * 40) / 2) + 10
        self.oy = 70
        self.Macierz = [[(0, 0) for i in range(s)] for j in range(w)]
        self.end = False
        self.stop = False
        self.win = False
        self.faul = False
        self.napis = "00000"
        self.losujBabe()

