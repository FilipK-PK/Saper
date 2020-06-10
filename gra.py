''' klasa tworzaca gre '''
import os
import random
import pygame

#scieszka katalogu z png
SCIERZKA = 'png'

#pobieram pola 1,2.. i baby
ZBIOR_ODKRYTYCH_IKON = {}
WARTOSCI_IKON_Z_CYFRAMI = (0, 1, 2, 3, 4, 5, 6, 7, 8, 'x', 'b', 'br', 'bp',)
NAZWY_IKON_PUL_Z_CYFRAMI = ('0.png', '1.png', '2.png', '3.png', '4.png',
                           '5.png', '6.png', '7.png', '8.png', 'bw.png',
                          'b.png', 'bw.png', 'bp.png')
for wartosc, nazwa in zip(WARTOSCI_IKON_Z_CYFRAMI, NAZWY_IKON_PUL_Z_CYFRAMI):
    ZBIOR_ODKRYTYCH_IKON.update(
       { wartosc:pygame.image.load(os.path.join(SCIERZKA, nazwa)) })

#pobieram pola okreslajace zakonczenie
ZBIOR_WYGRANA_PRZEGRANA = {}
NAZWY_IKON_WYGRANA_PRZEGRANA = ('w.png', 'k.png', 'zp.png')
NAZWA_KAFELKU_WYGRANA_PRZEGRANA = ('POLE_WYRGANA', 'POLE_PRZEGRANA',
                                   'POLE_ZASLEPKA_WY_PR')
for nazwa_kafelka, nazwa_pliku in zip(NAZWA_KAFELKU_WYGRANA_PRZEGRANA,
                                     NAZWY_IKON_WYGRANA_PRZEGRANA):
    ZBIOR_WYGRANA_PRZEGRANA.update({nazwa_kafelka
                           :pygame.image.load(os.path.join(SCIERZKA, nazwa_pliku))})

#pobieranie png przyciskow
PRZYCISK = {}
NAZWA_PLIKU_PRZYCISKU = ('PUSTY', 'RESET', 'FLAGA',
                        'BABY_PODGLAD', 'NIEPEWNOSC')
NAZWA_PRZYCISKU = ('p.png', 'r.png', 'f.png', 'br.png', 'z.png')
for nazwa_przycisku, nazwa_pliku in zip(NAZWA_PLIKU_PRZYCISKU,
                                       NAZWA_PRZYCISKU):
    PRZYCISK.update({nazwa_przycisku:pygame.image.load(
        os.path.join(SCIERZKA, nazwa_pliku))})

# pobieram pola wyswietlacza
ZNAKI_WYSWIETLACZA = []
NAZWY_IKON_WYSWIETLACZA = ('n0.png', 'n1.png', 'n2.png', 'n3.png', 'n4.png',
                          'n5.png', 'n6.png', 'n7.png', 'n8.png', 'n9.png',
                         'n-.png', 'nn.png')
for nazwa in NAZWY_IKON_WYSWIETLACZA:
    ZNAKI_WYSWIETLACZA.append(pygame.image.load(os.path.join(SCIERZKA, nazwa)))

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
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        self.baby = baby
        self.ilosc_bab = baby
        self.odstep_macierzy_od_boku = (int((600 - szerokosc * 
                                             SZEROKOSC_KAFELKA) / 2) + 10)
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

    def oznacz_babe(self, polozenie_y, polozenie_x):
        ''' ustawia odpowiednia wartosc pola na planszy '''
        # wartosci poczatkowe i koncowe
        poczatek_x = polozenie_x - 1
        poczatek_y = polozenie_y - 1
        koniec_x = polozenie_x + 1
        koniec_y = polozenie_y + 1

        # wartosci skrajne 0,n
        if polozenie_y == 0:
            poczatek_y = polozenie_y
        if polozenie_y == len(self.macierz) - 1:
            koniec_y = polozenie_y
        if polozenie_x == 0:
            poczatek_x = polozenie_x
        if polozenie_x == len(self.macierz[0]) - 1:
            koniec_x = polozenie_x

        # nanoszenie wartosci na plansze
        for i in range(poczatek_y, koniec_y + 1):
            for j in range(poczatek_x, koniec_x + 1):
                if self.macierz[i][j] != (ZNAK_BABY, STAN_NIC):
                    znak_pola = self.macierz[i][j][0]
                    self.macierz[i][j] = (znak_pola + 1, STAN_NIC)

    def rysuj_licznik_gry(self, surface):
        ''' rysowanie licznika bab, i obliczanie wartosci '''

        liczba_bab = abs(self.ilosc_bab)

         # rysowanie i okreslanie polorzenie liczby 1
        if liczba_bab < 100:
            # rysuje pole bez liczby
            surface.blit(ZNAKI_WYSWIETLACZA[11], GOR_LEW_ROG_1_LICZBY)
        else:
            surface.blit(ZNAKI_WYSWIETLACZA[liczba_bab//100],
                         GOR_LEW_ROG_1_LICZBY)
        liczba_bab = liczba_bab % 100

         # rysowanie i okreslanie polorzenie liczby 2
        if liczba_bab < 10:
            # rysuje pole bez liczby
            surface.blit(ZNAKI_WYSWIETLACZA[11], GOR_LEW_ROG_2_LICZBY)
        else:
            surface.blit(ZNAKI_WYSWIETLACZA[liczba_bab//10],
                         GOR_LEW_ROG_2_LICZBY)
        liczba_bab = liczba_bab % 10

         # rysowanie i okreslanie polorzenie liczby 3
        surface.blit(ZNAKI_WYSWIETLACZA[liczba_bab], GOR_LEW_ROG_3_LICZBY)

        # okreslanie minusa
        if self.ilosc_bab < 0:
            if self.ilosc_bab > -10:
                surface.blit(ZNAKI_WYSWIETLACZA[10], GOR_LEW_ROG_2_LICZBY)
            elif self.ilosc_bab > -100:
                surface.blit(ZNAKI_WYSWIETLACZA[10], GOR_LEW_ROG_1_LICZBY)

    def rysuj(self, surface):
        ''' rysuje wszystkich obiektow na ekranie planszy '''

        self.rysuj_licznik_gry(surface)  # rysowanie licznika bab

        # przycisk resetu
        surface.blit(PRZYCISK['RESET'], GOR_LEW_ROG_RESET)

        # rysowanie wygranej przegranej
        if self.win:
            surface.blit(ZBIOR_WYGRANA_PRZEGRANA['POLE_WYRGANA'],
                        GOR_LEW_ROG_WYGR_PRZE)
        elif self.end:
            surface.blit(ZBIOR_WYGRANA_PRZEGRANA['POLE_PRZEGRANA'],
                        GOR_LEW_ROG_WYGR_PRZE)
        else:
            surface.blit(ZBIOR_WYGRANA_PRZEGRANA['POLE_ZASLEPKA_WY_PR'],
                        GOR_LEW_ROG_WYGR_PRZE)

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
                        surface.blit(PRZYCISK['BABY_PODGLAD'], (yi, xi))
                    else:
                        surface.blit(PRZYCISK['PUSTY'], (yi, xi))# zwwykle pole
                elif self.macierz[y][x][1] == STAN_FLAGA:
                    surface.blit(PRZYCISK['FLAGA'], (yi, xi))  # oznacz bobe
                elif self.macierz[y][x][1] == STAN_ZAPYTANIE:
                    # oznacz niepewnosc
                    surface.blit(PRZYCISK['NIEPEWNOSC'], (yi, xi))

    def ruch(self):
        ''' nasluchuje wcisnietych klawisza myszki '''

        # sprawdza wcisniecie lewego klawisza myszy
        if pygame.mouse.get_pressed()[0]:
            kursor = pygame.mouse.get_pos()

            # czy wcisnieto reser
            if (POLOZENIE_RESET[3] < kursor[0] < POLOZENIE_RESET[1] 
                and POLOZENIE_RESET[0] < kursor[1] < POLOZENIE_RESET[2]):
                self.reset()

            # czy wcisnieto jakies pole kafelkow
            elif (self.odstep_macierzy_od_boku < kursor[0] < 
                    SZEROKOSC_OKNA - self.odstep_macierzy_od_boku 
                    and self.odstep_macierzy_od_gory < kursor[1] < 
                    self.odstep_macierzy_od_gory 
                    + len(self.macierz) * SZEROKOSC_KAFELKA
                    and not self.stop):

                # okreslanie ktory kafelek wcisnieto
                y = ((kursor[1] - self.odstep_macierzy_od_gory) //
                    SZEROKOSC_KAFELKA)
                x = ((kursor[0] - self.odstep_macierzy_od_boku) //
                    SZEROKOSC_KAFELKA)

                # co ma sie stac gdy pole jest puste lub niepewne
                if (self.macierz[y][x][1] == STAN_NIC
                        or self.macierz[y][x][1] == STAN_ZAPYTANIE):
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
            if (self.odstep_macierzy_od_boku < kursor[0]
                    < SZEROKOSC_OKNA - self.odstep_macierzy_od_boku
                and self.odstep_macierzy_od_gory < kursor[1]
                    < self.odstep_macierzy_od_gory
                + len(self.macierz) * SZEROKOSC_KAFELKA and not self.stop):

                # okreslanie ktory kafelek wcisnieto
                y = ((kursor[1] - self.odstep_macierzy_od_gory) //
                    SZEROKOSC_KAFELKA)
                x = ((kursor[0] - self.odstep_macierzy_od_boku) //
                    SZEROKOSC_KAFELKA)

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
        for i in range(self.wysokosc):
            for j in range(self.szerokosc):
                if self.macierz[i][j] == (ZNAK_BABY, STAN_NIC):
                    self.macierz[i][j] = ('b', STAN_ODKRYTY)
                if (self.macierz[i][j][1] == STAN_FLAGA
                        and self.macierz[i][j][0] != ZNAK_BABY):
                    self.macierz[i][j] = ('bp', STAN_ODKRYTY)

        self.macierz[y][x] = (ZNAK_BABY, STAN_ODKRYTY)
        # zatrymuje gre i uruchamiam flage przegranej
        self.stop = True
        self.end = True

    def odkryj(self, y, x):
        ''' odkrywa pole na planszy '''
        pole_odkryte = (0, 1)

        PUNKTY_OKREZNE = [{'y': -1, 'x': -1}, {'y': -1, 'x': 0}, {'y': -1, 'x': 1},
                  {'y': 0, 'x': 1}, {'y': 1, 'x': 1}, {'y': 1, 'x': 0},
                  {'y': 1, 'x': -1}, {'y': 0, 'x': -1}]

        for p in PUNKTY_OKREZNE:
            if not 0 <= y + p['y'] < len(self.macierz):
                continue
            if not 0 <= x + p['x'] < len(self.macierz[y]):
                continue
            if not self.macierz[y + p['y']][x + p['x']] == POLE_PUSTE:
                continue

            self.macierz[y + p['y']][x + p['x']] = pole_odkryte
            self.odznacz(y + p['y'], x + p['x'])
            self.odkryj(y + p['y'], x + p['x'])

    def odznacz(self, polozenie_y, polozenie_x):
        ''' odkrywa pola wokol odkrytego elementu'''

        # wartosci poczatkowe i koncowe odblokowwanych elementow
        poczatek_x = polozenie_x - 1
        poczatek_y = polozenie_y - 1
        koniec_x = polozenie_x + 1
        koniec_y = polozenie_y + 1

        # wartosci skrajne 0,n
        if polozenie_y == 0:
            poczatek_y = polozenie_y
        if polozenie_y == len(self.macierz) - 1:
            koniec_y = polozenie_y
        if polozenie_x == 0:
            poczatek_x = polozenie_x
        if polozenie_x == len(self.macierz[0]) - 1:
            koniec_x = polozenie_x

        # nanoszenie wartosci na plansze
        for i in range(poczatek_y, koniec_y + 1):
            for j in range(poczatek_x, koniec_x + 1):
                if 0 < self.macierz[i][j][0] < 8:
                    znak_pola = self.macierz[i][j][0]
                    self.macierz[i][j] = (znak_pola, STAN_ODKRYTY)

    def koniec(self):  # sprawdza czy wszysktie pola bez miny zostaly odkryte
        ''' sprawdza czy gracz wygral ture '''
        liczba_zakrytych_bab = 0
        liczba_odkrytych_pul = 0
        for i in range(self.wysokosc):
            for j in range(self.szerokosc):
                if (self.macierz[i][j] == (ZNAK_BABY, STAN_FLAGA)
                        or (self.macierz[i][j][0] == ZNAK_BABY and self.faul)):
                    liczba_zakrytych_bab += 1
                if self.macierz[i][j][1] == STAN_ODKRYTY:
                    liczba_odkrytych_pul += 1

        if (liczba_zakrytych_bab + liczba_odkrytych_pul ==
                len(self.macierz)*len(self.macierz[0])):
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
