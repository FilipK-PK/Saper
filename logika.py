import pygame
import random

class Logika():
    def __init__(self, s, w, b):
        self.w = w
        self.s = s
        self.b = b
        self.liczbikB = self.b
        self.end = False
        self.stop = False
        self.win = False
        self.faul = False
        self.napis = "00000"

        self.Macierz = [[(0, 0) for i in range(s)] for j in range(w)]
        self.losujBabe()

    def losujBabe(self):
        for i in range(self.b):
            x = random.randint(0, len(self.Macierz)-1)
            y = random.randint(0, len(self.Macierz[0])-1)

            while self.Macierz[x][y][0] == 'x':
                x = random.randint(0, len(self.Macierz)-1)
                y = random.randint(0, len(self.Macierz[0])-1)

            self.Macierz[x][y] = ('x', 0)
            self.oznaczBabe(x, y)

    def oznaczBabe(self, x, y):
        sx = x - 1
        sy = y - 1

        kx = x + 1
        ky = y + 1

        if x == 0:
            sx = x
        if x == len(self.Macierz) - 1:
            kx = x
        if y == 0:
            sy = y
        if y == len(self.Macierz[0]) - 1:
            ky = y

        for i in range(sx, kx + 1):
            for j in range(sy, ky + 1):
                if self.Macierz[i][j] != ('x', 0):
                    z = self.Macierz[i][j][0]
                    self.Macierz[i][j] = (z+1, 0)

    def ruch(self):
        if pygame.mouse.get_pressed()[0]:
            p = pygame.mouse.get_pos()

            if p[1]< 70:
                self.pasek(p);

            elif p[0] > self.ox and p[0] < 620 - self.ox and p[1] > self.oy and p[1] < self.oy + len(self.Macierz) * 40 and self.stop == False:
                y = (p[1] - self.oy) // 40
                x = (p[0] - self.ox) // 40

                if self.Macierz[y][x][1] == 0 or self.Macierz[y][x][1] == 3:
                    z = self.Macierz[y][x][0]
                    self.Macierz[y][x] = (z, 1)

                    if self.Macierz[y][x][0] == 0:
                        self.odznacz(y,x)
                        self.odkryj(y,x)

                    if self.Macierz[y][x][0] == 'x':
                        self.wybuch(x,y)

                    #self.wyswietl_g()

        elif pygame.mouse.get_pressed()[2]:
            p = pygame.mouse.get_pos()
            if p[0] > self.ox and p[0] < 620 - self.ox and p[1] > self.oy and p[1] < self.oy + len(self.Macierz) * 40 and self.stop == False:
                y = (p[1] - self.oy) // 40
                x = (p[0] - self.ox) // 40

                if self.Macierz[y][x][1] == 0:
                    z = self.Macierz[y][x][0]
                    self.Macierz[y][x] = (z, 2)
                    self.liczbikB -= 1

                elif self.Macierz[y][x][1] == 2:
                    z = self.Macierz[y][x][0]
                    self.Macierz[y][x] = (z, 3)
                    self.liczbikB += 1

                elif self.Macierz[y][x][1] == 3:
                    z = self.Macierz[y][x][0]
                    self.Macierz[y][x] = (z, 0)

    def wybuch(self, x, y):
        for i in range(len(self.Macierz)):
            for j in range(len(self.Macierz[i])):
                if self.Macierz[i][j] == ('x', 0):
                    self.Macierz[i][j] = ('b', 1)
                if self.Macierz[i][j][1] == 2 and self.Macierz[i][j][0] != 'x':
                    self.Macierz[i][j] = ('bp', 1)

        self.Macierz[y][x] = ('x', 1)
        self.stop = True
        self.end = True

    def odkryj(self, x, y):
        if x > 0 and y > 0 and self.Macierz[x - 1][y - 1] == (0, 0):
            self.Macierz[x - 1][y - 1] = (0, 1)
            self.odznacz(x - 1, y - 1)
            self.odkryj(x - 1, y - 1)

        if y > 0 and self.Macierz[x][y - 1] == (0, 0):
            self.Macierz[x][y - 1] = (0, 1)
            self.odznacz(x, y - 1)
            self.odkryj(x, y - 1)

        if x < len(self.Macierz)-1 and y > 0 and self.Macierz[x + 1][y - 1] == (0, 0):
            self.Macierz[x + 1][y - 1] = (0, 1)
            self.odznacz(x + 1, y - 1)
            self.odkryj(x + 1, y - 1)

        if x < len(self.Macierz)-1 and self.Macierz[x + 1][y] == (0, 0):
            self.Macierz[x + 1][y] = (0, 1)
            self.odznacz(x + 1, y)
            self.odkryj(x + 1, y)

        if x < len(self.Macierz)-1 and y < len(self.Macierz[0])-1 and self.Macierz[x + 1][y + 1] == (0, 0):
            self.Macierz[x + 1][y + 1] = (0, 1)
            self.odznacz(x + 1, y + 1)
            self.odkryj(x + 1, y + 1)

        if y < len(self.Macierz[0])-1 and self.Macierz[x][y + 1] == (0, 0):
            self.Macierz[x][y + 1] = (0, 1)
            self.odznacz(x, y + 1)
            self.odkryj(x, y + 1)

        if x > 0 and y < len(self.Macierz[0])-1 and self.Macierz[x - 1][y + 1] == (0, 0):
            self.Macierz[x - 1][y + 1] = (0, 1)
            self.odznacz(x - 1, y + 1)
            self.odkryj(x - 1, y + 1)

        if x > 0 and self.Macierz[x - 1][y] == (0, 0):
            self.Macierz[x - 1][y] = (0, 1)
            self.odznacz(x - 1, y)
            self.odkryj(x - 1, y)

    def odznacz(self, x, y):
        sx = x - 1
        sy = y - 1

        kx = x + 1
        ky = y + 1

        if x == 0:
            sx = x
        if x == self.w-1:
            kx = x
        if y == 0:
            sy = y
        if y == self.s-1:
            ky = y

        for i in range(sx, kx + 1):
            for j in range(sy, ky + 1):
                if self.Macierz[i][j][0] > 0 and self.Macierz[i][j][0] < 8:
                    z = self.Macierz[i][j][0]
                    self.Macierz[i][j] = (z, 1)

    def koniec(self):
        c = 0
        d = 0
        for i in range(len(self.Macierz)):
            for j in range(len(self.Macierz[0])):
                if self.Macierz[i][j] == ('x', 2) or (self.Macierz[i][j][0] == 'x' and self.faul):
                    c += 1
                if self.Macierz[i][j][1] == 1:
                    d += 1

        if c + d == len(self.Macierz)*len(self.Macierz[0]):
            self.stop = True
            self.win = True

    def reset(self):
        for i in range(len(self.Macierz)):
            for j in range(len(self.Macierz[0])):
                self.Macierz[i][j] = (0,0)

        self.losujBabe()
        self.stop = False
        self.end = False
        self.win = False
        self.faul = False
        self.liczbikB = self.b
        self.napis = "00000"

    def pasek(self, p):
        if p[0] > 215 and p[0] < 405 and p[1] > 10 and p[1] < 60:
            self.reset()

    def klik(self, c):
        self.napis  = self.napis[1:] + chr(c)

        print(self.napis)
        if self.napis == "xyzzy":
            self.faul = True
            print("FAIL")