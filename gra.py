import pygame
import random
import math
import os

# pobieranie grafiki
POLE_0 = pygame.image.load(os.path.join('png','0.png'))
POLE_1 = pygame.image.load(os.path.join('png','1.png'))
POLE_2 = pygame.image.load(os.path.join('png','2.png'))
POLE_3 = pygame.image.load(os.path.join('png','3.png'))
POLE_4 = pygame.image.load(os.path.join('png','4.png'))
POLE_5 = pygame.image.load(os.path.join('png','5.png'))
POLE_6 = pygame.image.load(os.path.join('png','6.png'))
POLE_7 = pygame.image.load(os.path.join('png','7.png'))
POLE_8 = pygame.image.load(os.path.join('png','8.png'))

POLE_BABY = pygame.image.load(os.path.join('png','b.png'))
POLE_BABY_BUM = pygame.image.load(os.path.join('png','bw.png'))
POLE_BLAD_FLAGI = pygame.image.load(os.path.join('png','bp.png'))
POLE_WYRGANA = pygame.image.load(os.path.join('png','w.png'))
POLE_PRZEGRANA = pygame.image.load(os.path.join('png','k.png'))
POLE_ZASLEPKA_WY_PR = pygame.image.load(os.path.join('png','zp.png'))

PRZYCISK_PUSTY = pygame.image.load(os.path.join('png','p.png'))
PRZYCISK_RESET = pygame.image.load(os.path.join('png','r.png'))
PRZYCISK_FLAFI = pygame.image.load(os.path.join('png','f.png'))
PRZYCISK_BABY_PODGLAD = pygame.image.load(os.path.join('png','br.png'))
PRZYCISK_NIEPEWNOSCI = pygame.image.load(os.path.join('png','z.png'))

LICZBA_0 = pygame.image.load(os.path.join('png','n0.png'))
LICZBA_1 = pygame.image.load(os.path.join('png','n1.png'))
LICZBA_2 = pygame.image.load(os.path.join('png','n2.png'))
LICZBA_3 = pygame.image.load(os.path.join('png','n3.png'))
LICZBA_4 = pygame.image.load(os.path.join('png','n4.png'))
LICZBA_5 = pygame.image.load(os.path.join('png','n5.png'))
LICZBA_6 = pygame.image.load(os.path.join('png','n6.png'))
LICZBA_7 = pygame.image.load(os.path.join('png','n7.png'))
LICZBA_8 = pygame.image.load(os.path.join('png','n8.png'))
LICZBA_9 = pygame.image.load(os.path.join('png','n9.png'))
LICZBA_MINUS = pygame.image.load(os.path.join('png','n-.png'))
LICZBA_BRAK = pygame.image.load(os.path.join('png','nn.png'))

#zmienne globalne
SZEROKOSC_KAFELKA = 40
GOR_LEW_ROG_1_LICZBY = (20, 10)
GOR_LEW_ROG_2_LICZBY = (50, 10)
GOR_LEW_ROG_3_LICZBY = (80, 10)
GOR_LEW_ROG_WYGR_PRZE = (440,5)
GOR_LEW_ROG_RESET = (215,10)

ZBIOR_ODKRYTYCH_IKON = {0:POLE_0, 1:POLE_1, 2:POLE_2, 3:POLE_3, 4:POLE_4, 5:POLE_5, 6:POLE_6, 7:POLE_7, 8:POLE_8,
                        'x':POLE_BABY_BUM, 'b':POLE_BABY, 'br':POLE_BLAD_FLAGI,'bp':POLE_BLAD_FLAGI}

ZNAKI_WYSWIETLACZA = (LICZBA_0, LICZBA_1, LICZBA_2, LICZBA_3, LICZBA_4, LICZBA_5, LICZBA_6, LICZBA_7, LICZBA_8, LICZBA_9)

class Gra():
    def __init__(self, s, w, b):
        self.b = b
        self.liczbikB = self.b
        self.pocz_plan_na_ekr_X = int((600 - s * SZEROKOSC_KAFELKA) / 2) + 10
        self.pocz_plan_na_ekr_Y = 70
        self.end = False
        self.stop = False
        self.win = False
        self.faul = False
        self.napis = "00000"

        self.Macierz = [[(0, 0) for i in range(s)] for j in range(w)]
        self.losuj_Babe()

    def losuj_Babe(self):#losowanie bab
        for i in range(self.b):
            x = random.randint(0, len(self.Macierz)-1)
            y = random.randint(0, len(self.Macierz[0])-1)

            #wykonuje sie dopuki baba nie jest na babie
            while self.Macierz[x][y][0] == 'x':
                x = random.randint(0, len(self.Macierz)-1)
                y = random.randint(0, len(self.Macierz[0])-1)

            #nanoszenie baby na plansze
            self.Macierz[x][y] = ('x', 0)
            self.oznacz_Babe(x, y)

    def oznacz_Babe(self, x, y):#zwieksza wartoscc pola wokol baby o wartosc
        #wartosci poczatkowe i koncowe
        StartX = x - 1
        StartY = y - 1
        KoniecX = x + 1
        KoniecY = y + 1

        #wartosci skrajne 0,n
        if x == 0:
            StartX = x
        if x == len(self.Macierz) - 1:
            KoniecX = x
        if y == 0:
            StartY = y
        if y == len(self.Macierz[0]) - 1:
            KoniecY = y

        #nanoszenie wartosci na plansze
        for i in range(StartX, KoniecX + 1):
            for j in range(StartY, KoniecY + 1):
                if self.Macierz[i][j] != ('x', 0):
                    z = self.Macierz[i][j][0]
                    self.Macierz[i][j] = (z+1, 0)

    def rys_Licznik(self,surface):# rysowanie licznika bab

        x = abs(self.liczbikB)

        #rysowanie i okreslanie połorzenie liczby 1
        if x < 100:
            surface.blit(LICZBA_BRAK, GOR_LEW_ROG_1_LICZBY)
        else:
            surface.blit(ZNAKI_WYSWIETLACZA[x//100], GOR_LEW_ROG_1_LICZBY)
        x = x % 100

        # rysowanie i okreslanie połorzenie liczby 2
        if x < 10:
            surface.blit(LICZBA_BRAK, GOR_LEW_ROG_2_LICZBY)
        else:
            surface.blit(ZNAKI_WYSWIETLACZA[x//10], GOR_LEW_ROG_2_LICZBY)
        x = x % 10

        # rysowanie i okreslanie połorzenie liczby 3
        surface.blit(ZNAKI_WYSWIETLACZA[x], GOR_LEW_ROG_3_LICZBY)

        #okreslanie minusa
        if self.liczbikB < 0:
            if self.liczbikB > -10:
                surface.blit(LICZBA_MINUS, GOR_LEW_ROG_2_LICZBY)
            elif self.liczbikB > -100:
                surface.blit(LICZBA_MINUS, GOR_LEW_ROG_1_LICZBY)

    def rysuj(self, surface):# rysowanie wszystkich obiektów na ekranie planszy
        self.rys_Licznik(surface)#rysowanie licznika bab

        #przycisk resetu
        surface.blit(PRZYCISK_RESET, GOR_LEW_ROG_RESET)

        #rysowanie wygranej przegranej
        if self.win:
            surface.blit(POLE_WYRGANA, GOR_LEW_ROG_WYGR_PRZE)
        elif self.end:
            surface.blit(POLE_PRZEGRANA, GOR_LEW_ROG_WYGR_PRZE)
        else:
            surface.blit(POLE_ZASLEPKA_WY_PR, GOR_LEW_ROG_WYGR_PRZE)

        #rysowanie przyciskow do odblokowania
        for y in range(len(self.Macierz)):
            for x in range(len(self.Macierz[y])):
                xi = self.pocz_plan_na_ekr_X + x * SZEROKOSC_KAFELKA
                yi = self.pocz_plan_na_ekr_Y + y * SZEROKOSC_KAFELKA

                if self.Macierz[y][x][1] == 1:#pokaz odkryte pole
                    surface.blit( ZBIOR_ODKRYTYCH_IKON[self.Macierz[y][x][0]], (xi, yi))
                elif self.Macierz[y][x][1] == 0:#pokaz nieruszone pola
                    if self.Macierz[y][x][0] == 'x' and self.faul:# pokaz podglad baby
                        surface.blit(PRZYCISK_BABY_PODGLAD, (xi, yi))
                    else:
                        surface.blit(PRZYCISK_PUSTY, (xi, yi))#zwwykłe pole
                elif self.Macierz[y][x][1] == 2:
                    surface.blit(PRZYCISK_FLAFI, (xi, yi))#oznacz bobe
                elif self.Macierz[y][x][1] == 3:
                    surface.blit(PRZYCISK_NIEPEWNOSCI, (xi, yi))#oznacz niepewnosc

    def ruch(self):#nasluchuje wcisnietych klawiszy
        if pygame.mouse.get_pressed()[0]:#sprawdza wcisniecie lewego klawisza myszy
            p = pygame.mouse.get_pos()

            #czy wcisnieto reser
            if 215 < p[0] < 405 and 10 < p[1] < 60:
                self.reset()

            #czy wcisnieto jakies pole kafelkow
            elif self.pocz_plan_na_ekr_X < p[0] < 620 - self.pocz_plan_na_ekr_X \
                    and self.pocz_plan_na_ekr_Y < p[1] < self.pocz_plan_na_ekr_Y + len(self.Macierz) * SZEROKOSC_KAFELKA\
                    and self.stop == False:

               #okreslanie ktory kafelek wcisnieto
                y = (p[1] - self.pocz_plan_na_ekr_Y) // SZEROKOSC_KAFELKA
                x = (p[0] - self.pocz_plan_na_ekr_X) // SZEROKOSC_KAFELKA

                #co ma sie stac gdy pole jest puste lub niepewne
                if self.Macierz[y][x][1] == 0 or self.Macierz[y][x][1] == 3:
                    z = self.Macierz[y][x][0]
                    self.Macierz[y][x] = (z, 1)

                    #jesli puste to odkryj
                    if self.Macierz[y][x][0] == 0:
                        self.odkryj(y,x)
                        self.odznacz(y,x)

                    #jesli baba to uruchom inne baby
                    if self.Macierz[y][x][0] == 'x':
                        self.wybuch(x,y)


        elif pygame.mouse.get_pressed()[2]:#sprawdza wcisniecie prawego klawisza myszy
            p = pygame.mouse.get_pos()

            # czy wcisnieto jakies pole kafelkow
            if self.pocz_plan_na_ekr_X < p[0] < 620 - self.pocz_plan_na_ekr_X \
                    and self.pocz_plan_na_ekr_Y < p[1] < self.pocz_plan_na_ekr_Y + len(self.Macierz) * SZEROKOSC_KAFELKA\
                    and self.stop == False:

                # okreslanie ktory kafelek wcisnieto
                y = (p[1] - self.pocz_plan_na_ekr_Y) // SZEROKOSC_KAFELKA
                x = (p[0] - self.pocz_plan_na_ekr_X) // SZEROKOSC_KAFELKA

                #jesli pole bylo puste to ustaw zabespieczone
                if self.Macierz[y][x][1] == 0:
                    z = self.Macierz[y][x][0]
                    self.Macierz[y][x] = (z, 2)
                    self.liczbikB -= 1

                # jesli pole bylo zabespieczone to ustaw niepewne
                elif self.Macierz[y][x][1] == 2:
                    z = self.Macierz[y][x][0]
                    self.Macierz[y][x] = (z, 3)
                    self.liczbikB += 1

                # jesli pole bylo niepewne to ustaw puste
                elif self.Macierz[y][x][1] == 3:
                    z = self.Macierz[y][x][0]
                    self.Macierz[y][x] = (z, 0)

    def wybuch(self, x, y):# odblokowuje pozostałe baby
        for i in range(len(self.Macierz)):
            for j in range(len(self.Macierz[i])):
                if self.Macierz[i][j] == ('x', 0):
                    self.Macierz[i][j] = ('b', 1)
                if self.Macierz[i][j][1] == 2 and self.Macierz[i][j][0] != 'x':
                    self.Macierz[i][j] = ('bp', 1)

        self.Macierz[y][x] = ('x', 1)
        #zatrymuje gre i uruchamiam flage przegranej
        self.stop = True
        self.end = True

    def odkryj(self, x, y):# jesli nacisnieto pole puste, przeszukuje wszystkie wokolo czo sa puste
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

    def odznacz(self, x, y):#odblokowuje pola wokul danego pola
        #wartosci poczatkowe i koncowe odblokowwanych elementow
        StartX = x - 1
        StartY = y - 1
        KoniecX = x + 1
        KoniecY = y + 1

        # skrajne przypadki 0, n
        if x == 0:
            StartX = x
        if x == len(self.Macierz)-1:
            KoniecX = x
        if y == 0:
            StartY = y
        if y == len(self.Macierz[0])-1:
            KoniecY = y

        #odznaczanie pol
        for i in range(StartX, KoniecX + 1):
            for j in range(StartY, KoniecY + 1):
                if 0 < self.Macierz[i][j][0] < 8:
                    z = self.Macierz[i][j][0]
                    self.Macierz[i][j] = (z, 1)

    def koniec(self):#sprawdza czy wszysktie pola bez miny zostały odznaczone
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

    def reset(self):#przywraca wartosci poczatkowe
        for i in range(len(self.Macierz)):
            for j in range(len(self.Macierz[0])):
                self.Macierz[i][j] = (0,0)

        self.losuj_Babe()
        self.stop = False
        self.end = False
        self.win = False
        self.faul = False
        self.liczbikB = self.b
        self.napis = "00000"

    def klik(self, c):#sprawdza wprowadzenie kodu xyzzy
        self.napis  = self.napis[1:] + chr(c)

        if self.napis == "xyzzy":#uruchamia podglad bab
            self.faul = True
            print("FAIL")