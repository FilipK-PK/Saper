''' klasa tworzaca gre '''
import os
import random
import pygame

POLE_0 = pygame.image.load(os.path.join('png/0.png'))
POLE_1 = pygame.image.load(os.path.join('png/1.png'))
POLE_2 = pygame.image.load(os.path.join('png/2.png'))
POLE_3 = pygame.image.load(os.path.join('png/3.png'))
POLE_4 = pygame.image.load(os.path.join('png/4.png'))
POLE_5 = pygame.image.load(os.path.join('png/5.png'))
POLE_6 = pygame.image.load(os.path.join('png/6.png'))
POLE_7 = pygame.image.load(os.path.join('png/7.png'))
POLE_8 = pygame.image.load(os.path.join('png/8.png'))

POLE_BABY = pygame.image.load(os.path.join('png/b.png'))
POLE_BABY_BUM = pygame.image.load(os.path.join('png/bw.png'))
POLE_BLAD_FLAGI = pygame.image.load(os.path.join('png/bp.png'))
POLE_WYRGANA = pygame.image.load(os.path.join('png/w.png'))
POLE_PRZEGRANA = pygame.image.load(os.path.join('png/k.png'))
POLE_ZASLEPKA_WY_PR = pygame.image.load(os.path.join('png/zp.png'))

PRZYCISK_PUSTY = pygame.image.load(os.path.join('png/p.png'))
PRZYCISK_RESET = pygame.image.load(os.path.join('png/r.png'))
PRZYCISK_FLAFI = pygame.image.load(os.path.join('png/f.png'))
PRZYCISK_BABY_PODGLAD = pygame.image.load(os.path.join('png/br.png'))
PRZYCISK_NIEPEWNOSCI = pygame.image.load(os.path.join('png/z.png'))

LICZBA_0 = pygame.image.load(os.path.join('png/n0.png'))
LICZBA_1 = pygame.image.load(os.path.join('png/n1.png'))
LICZBA_2 = pygame.image.load(os.path.join('png/n2.png'))
LICZBA_3 = pygame.image.load(os.path.join('png/n3.png'))
LICZBA_4 = pygame.image.load(os.path.join('png/n4.png'))
LICZBA_5 = pygame.image.load(os.path.join('png/n5.png'))
LICZBA_6 = pygame.image.load(os.path.join('png/n6.png'))
LICZBA_7 = pygame.image.load(os.path.join('png/n7.png'))
LICZBA_8 = pygame.image.load(os.path.join('png/n8.png'))
LICZBA_9 = pygame.image.load(os.path.join('png/n9.png'))
LICZBA_MINUS = pygame.image.load(os.path.join('png/n-.png'))
LICZBA_BRAK = pygame.image.load(os.path.join('png/nn.png'))

# zmienne globalne
SZEROKOSC_KAFELKA = 40
SZEROKOSC_OKNA = 620
GOR_LEW_ROG_1_LICZBY = (20, 10)
GOR_LEW_ROG_2_LICZBY = (50, 10)
GOR_LEW_ROG_3_LICZBY = (80, 10)
GOR_LEW_ROG_WYGR_PRZE = (440, 5)
GOR_LEW_ROG_RESET = (215, 10)
POLOZENIE_RESET = (10, 405, 60, 215)
STAN_FLAGA = 2
STAN_ZAPYTANIE = 3
STAN_NIC = 0
STAN_ODKRYTY = 1
POLE_PUSTE = (0, 0)
ZNAK_BABY = 'x'
ZNAK_PUSTY = 0

ZBIOR_ODKRYTYCH_IKON = {0: POLE_0, 1: POLE_1, 2: POLE_2, 3: POLE_3,
                        4: POLE_4, 5: POLE_5, 6: POLE_6, 7: POLE_7,
                        8: POLE_8, 'x': POLE_BABY_BUM, 'b': POLE_BABY,
                        'br': POLE_BLAD_FLAGI, 'bp': POLE_BLAD_FLAGI}

ZNAKI_WYSWIETLACZA = (LICZBA_0, LICZBA_1, LICZBA_2, LICZBA_3, LICZBA_4,
                      LICZBA_5, LICZBA_6, LICZBA_7, LICZBA_8, LICZBA_9)

class Plansza:
    ''' klasa tworzaca macierz do klasy Gra '''

    def __init__(self, wysokosc, szerokosc):
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc

    #  tworze macierz z czystymi polami do wypelnienia
    def twoz(self):
        ''' zwraca czysta macierz do Gry '''

        return [[POLE_PUSTE for _ in range(self.szerokosc)]
                for _ in range(self.wysokosc)]


class Gra:
    ''' klasa tworzaca gre saper '''
    def __init__(self, wysokosc, szerokosc, baby):
        self.baby = baby
        self.ilosc_bab = baby
        self.odstep_macierzy_od_boku = \
            int((600 - szerokosc * SZEROKOSC_KAFELKA) / 2) + 10
        self.odstep_macierzy_od_gory = 70
        self.end = False
        self.stop = False
        self.win = False
        self.faul = False
        self.napis = "00000"
        self.macierz = Plansza(wysokosc, szerokosc).twoz()
        self.rozmiesc_baby()

    def rozmiesc_baby(self):
        ''' losowanie bab na planszy '''

        for _ in range(self.baby):
            y = random.randint(0, len(self.macierz) - 1)
            x = random.randint(0, len(self.macierz[0]) - 1)

            # wykonuje sie dopuki baba nie jest na babie
            while self.macierz[y][x][0] == ZNAK_BABY:
                y = random.randint(0, len(self.macierz) - 1)
                x = random.randint(0, len(self.macierz[0]) - 1)

            # nanoszenie baby na plansze
            self.macierz[y][x] = (ZNAK_BABY, STAN_NIC)
            self.oznacz_babe(y, x)

    def oznacz_babe(self, polozenie_x, polozenie_y):
        ''' ustawia odpowiednia wartosc pola na planszy '''
        # wartosci poczatkowe i koncowe
        poczatek_x = polozenie_x - 1
        poczatek_y = polozenie_y - 1
        koniec_x = polozenie_x + 1
        koniec_y = polozenie_y + 1

        # wartosci skrajne 0,n
        if polozenie_x == 0:
            poczatek_x = polozenie_x
        if polozenie_x == len(self.macierz) - 1:
            koniec_x = polozenie_x
        if polozenie_y == 0:
            poczatek_y = polozenie_y
        if polozenie_y == len(self.macierz[0]) - 1:
            koniec_y = polozenie_y

        # nanoszenie wartosci na plansze
        for i in range(poczatek_x, koniec_x + 1):
            for j in range(poczatek_y, koniec_y + 1):
                if self.macierz[i][j] != (ZNAK_BABY, STAN_NIC):
                    znak_pola = self.macierz[i][j][0]
                    self.macierz[i][j] = (znak_pola + 1, STAN_NIC)

    def rysuj_licznik_gry(self, surface):
        ''' rysowanie licznika bab, i obliczanie wartosci '''

        liczba_bab = abs(self.ilosc_bab)

         # rysowanie i okreslanie polorzenie liczby 1
        if liczba_bab < 100:
            surface.blit(LICZBA_BRAK, GOR_LEW_ROG_1_LICZBY)
        else:
            surface.blit(ZNAKI_WYSWIETLACZA[liczba_bab//100],
                         GOR_LEW_ROG_1_LICZBY)
        liczba_bab = liczba_bab % 100

         # rysowanie i okreslanie polorzenie liczby 2
        if liczba_bab < 10:
            surface.blit(LICZBA_BRAK, GOR_LEW_ROG_2_LICZBY)
        else:
            surface.blit(ZNAKI_WYSWIETLACZA[liczba_bab//10],
                         GOR_LEW_ROG_2_LICZBY)
        liczba_bab = liczba_bab % 10

         # rysowanie i okreslanie polorzenie liczby 3
        surface.blit(ZNAKI_WYSWIETLACZA[liczba_bab], GOR_LEW_ROG_3_LICZBY)

        # okreslanie minusa
        if self.ilosc_bab < 0:
            if self.ilosc_bab > -10:
                surface.blit(LICZBA_MINUS, GOR_LEW_ROG_2_LICZBY)
            elif self.ilosc_bab > -100:
                surface.blit(LICZBA_MINUS, GOR_LEW_ROG_1_LICZBY)

    def rysuj(self, surface):
        ''' rysuje wszystkich obiektow na ekranie planszy '''

        self.rysuj_licznik_gry(surface)  # rysowanie licznika bab

        # przycisk resetu
        surface.blit(PRZYCISK_RESET, GOR_LEW_ROG_RESET)

        # rysowanie wygranej przegranej
        if self.win:
            surface.blit(POLE_WYRGANA, GOR_LEW_ROG_WYGR_PRZE)
        elif self.end:
            surface.blit(POLE_PRZEGRANA, GOR_LEW_ROG_WYGR_PRZE)
        else:
            surface.blit(POLE_ZASLEPKA_WY_PR, GOR_LEW_ROG_WYGR_PRZE)

        # rysowanie przyciskow do odblokowania
        for y in range(len(self.macierz)):
            for x in range(len(self.macierz[y])):
                yi = self.odstep_macierzy_od_boku + x * SZEROKOSC_KAFELKA
                xi = self.odstep_macierzy_od_gory + y * SZEROKOSC_KAFELKA

                if self.macierz[y][x][1] == STAN_ODKRYTY:# pokaz odkryte pole
                    surface.blit(ZBIOR_ODKRYTYCH_IKON[self.macierz[y][x][0]],
                                 (yi, xi))
                elif self.macierz[y][x][1] == STAN_NIC:# pokaz nieruszone pola
                    # pokaz podglad baby
                    if self.macierz[y][x][0] == ZNAK_BABY and self.faul:
                        surface.blit(PRZYCISK_BABY_PODGLAD, (yi, xi))
                    else:
                        surface.blit(PRZYCISK_PUSTY, (yi, xi))  # zwwykle pole
                elif self.macierz[y][x][1] == STAN_FLAGA:
                    surface.blit(PRZYCISK_FLAFI, (yi, xi))  # oznacz bobe
                elif self.macierz[y][x][1] == STAN_ZAPYTANIE:
                    # oznacz niepewnosc
                    surface.blit(PRZYCISK_NIEPEWNOSCI, (yi, xi))

    def ruch(self):
        ''' nasluchuje wcisnietych klawisza myszki '''

        # sprawdza wcisniecie lewego klawisza myszy
        if pygame.mouse.get_pressed()[0]:
            kursor = pygame.mouse.get_pos()

            # czy wcisnieto reser
            if POLOZENIE_RESET[3] < kursor[0] < POLOZENIE_RESET[1]\
                    and POLOZENIE_RESET[0] < kursor[1] < POLOZENIE_RESET[2]:
                self.reset()

            # czy wcisnieto jakies pole kafelkow
            elif self.odstep_macierzy_od_boku < kursor[0] < \
                    SZEROKOSC_OKNA - self.odstep_macierzy_od_boku \
                    and self.odstep_macierzy_od_gory < kursor[1] < \
                    self.odstep_macierzy_od_gory \
                    + len(self.macierz) * SZEROKOSC_KAFELKA\
                    and not self.stop:

                # okreslanie ktory kafelek wcisnieto
                y = (kursor[1] - self.odstep_macierzy_od_gory) // \
                    SZEROKOSC_KAFELKA
                x = (kursor[0] - self.odstep_macierzy_od_boku) // \
                    SZEROKOSC_KAFELKA

                # co ma sie stac gdy pole jest puste lub niepewne
                if self.macierz[y][x][1] == STAN_NIC \
                        or self.macierz[y][x][1] == STAN_ZAPYTANIE:
                    wartosc_pola = self.macierz[y][x][0]
                    self.macierz[y][x] = (wartosc_pola, STAN_ODKRYTY)

                    # jesli puste to odkryj
                    if self.macierz[y][x][0] == ZNAK_PUSTY:
                        self.odkryj(y, x)
                        self.odznacz(y, x)

                    # jesli baba to uruchom inne baby
                    if self.macierz[y][x][0] == ZNAK_BABY:
                        self.wybuch(x, y)

        # sprawdza wcisniecie prawego klawisza myszy
        elif pygame.mouse.get_pressed()[2]:
            kursor = pygame.mouse.get_pos()

            # czy wcisnieto jakies pole kafelkow
            if self.odstep_macierzy_od_boku < kursor[0] \
                    < SZEROKOSC_OKNA - self.odstep_macierzy_od_boku \
                and self.odstep_macierzy_od_gory < kursor[1] \
                    < self.odstep_macierzy_od_gory \
                + len(self.macierz) * SZEROKOSC_KAFELKA and not self.stop:

                # okreslanie ktory kafelek wcisnieto
                y = (kursor[1] - self.odstep_macierzy_od_gory) //\
                    SZEROKOSC_KAFELKA
                x = (kursor[0] - self.odstep_macierzy_od_boku) //\
                    SZEROKOSC_KAFELKA

                # jesli pole bylo puste to ustaw zabespieczone
                if self.macierz[y][x][1] == STAN_NIC:
                    wartosc_pola = self.macierz[y][x][0]
                    self.macierz[y][x] = (wartosc_pola, STAN_FLAGA)
                    self.ilosc_bab -= 1

                # jesli pole bylo zabespieczone to ustaw niepewne
                elif self.macierz[y][x][1] == STAN_FLAGA:
                    wartosc_pola = self.macierz[y][x][0]
                    self.macierz[y][x] = (wartosc_pola, STAN_ZAPYTANIE)
                    self.ilosc_bab += 1

                # jesli pole bylo niepewne to ustaw puste
                elif self.macierz[y][x][1] == STAN_ZAPYTANIE:
                    wartosc_pola = self.macierz[y][x][0]
                    self.macierz[y][x] = (wartosc_pola, STAN_NIC)

    def wybuch(self, x, y):
        ''' sprawdza wybranie baby, i odpala reszte bab '''
        for i in range(len(self.macierz)):
            for j in range(len(self.macierz[i])):
                if self.macierz[i][j] == (ZNAK_BABY, STAN_NIC):
                    self.macierz[i][j] = ('b', STAN_ODKRYTY)
                if self.macierz[i][j][1] == STAN_FLAGA \
                        and self.macierz[i][j][0] != ZNAK_BABY:
                    self.macierz[i][j] = ('bp', STAN_ODKRYTY)

        self.macierz[y][x] = (ZNAK_BABY, STAN_ODKRYTY)
        # zatrymuje gre i uruchamiam flage przegranej
        self.stop = True
        self.end = True

    def odkryj(self, y, x):
        ''' odkrywa pole na planszy '''
        pole_odkryte = (0, 1)

        punkty = [{'y': -1, 'x': -1}, {'y': -1, 'x': 0}, {'y': -1, 'x': 1},
                  {'y': 0, 'x': 1}, {'y': 1, 'x': 1}, {'y': 1, 'x': 0},
                  {'y': 1, 'x': -1}, {'y': 0, 'x': -1}]

        for p in punkty:
            if not 0 <= y + p['y'] < len(self.macierz):
                continue
            if not 0 <= x + p['x'] < len(self.macierz[y]):
                continue
            if not self.macierz[y + p['y']][x + p['x']] == POLE_PUSTE:
                continue

            self.macierz[y + p['y']][x + p['x']] = pole_odkryte
            self.odznacz(y + p['y'], x + p['x'])
            self.odkryj(y + p['y'], x + p['x'])

    def odznacz(self, y, x):
        ''' odkrywa pola wokol odkrytego elementu'''
        # wartosci poczatkowe i koncowe odblokowwanych elementow

        # odznaczanie pol
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
                if self.Macierz[i][j][0] > 0 and self.Macierz[i][j][0] < 8:
                    z = self.Macierz[i][j][0]
                    self.Macierz[i][j] = (z, 1)

    def koniec(self):  # sprawdza czy wszysktie pola bez miny zostaly odkryte
        ''' sprawdza czy gracz wygral ture '''
        liczba_zakrytych_bab = 0
        liczba_odkrytych_pul = 0
        for i in range(len(self.macierz)):
            for j in range(len(self.macierz[0])):
                if self.macierz[i][j] == (ZNAK_BABY, STAN_FLAGA) \
                        or (self.macierz[i][j][0] == ZNAK_BABY and self.faul):
                    liczba_zakrytych_bab += 1
                if self.macierz[i][j][1] == STAN_ODKRYTY:
                    liczba_odkrytych_pul += 1

        if liczba_zakrytych_bab + liczba_odkrytych_pul ==\
                len(self.macierz)*len(self.macierz[0]):
            self.stop = True
            self.win = True

    def reset(self):
        ''' przywraca wartosci poczatkowe, gra zaczyna sie od nowa'''
        wysokosc = len(self.macierz)
        szerokosc = len(self.macierz[0])
        self.macierz = Plansza(wysokosc, szerokosc).twoz()

        self.rozmiesc_baby()
        self.stop = False
        self.end = False
        self.win = False
        self.faul = False
        self.ilosc_bab = self.baby
        self.napis = "00000"

    def klik(self, znak):
        """ funkcja zapamietuje i sprawdza czy wpisano kod xyzzy """
        self.napis = self.napis[1:] + chr(znak)

        if self.napis == "xyzzy":  # uruchamia podglad bab
            self.faul = True
