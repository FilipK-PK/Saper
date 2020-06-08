''' klasa z oknem poczatkowym '''
import pygame
import tkinter
import tkinter.messagebox
from gra import Gra

WYMIARY_OKNA = (620, 680)
MAX_PLANSZY = 15
MIN_PLANSZY = 2
MAX_BAB = 3  # ilosci przyciskow/MAX_BAB to maksymalna liczba bab


# klasam wyjatkow
class Wyjatek(Exception):
    ''' klasa wyjatkow '''
    pass


class OknoStart:
    ''' klasa z oknem poczatkowym i sprawdzaniem ustawien '''
    def __init__(self):
        self.wartosci_start = (2, 2, 1)
        self.poprawnosc = False
        self.okno = tkinter.Tk()
        self.okno.title('SAPER')
        self.okno.geometry('300x200+100+100')

        okno1 = tkinter.Frame(self.okno)
        okno2 = tkinter.Frame(self.okno)
        okno3 = tkinter.Frame(self.okno)

        text1 = tkinter.Label(okno1, text='Podaj wymiary okna ')
        text2 = tkinter.Label(okno1, text='x')
        self.wpisz1 = tkinter.Entry(okno1, width=3)
        self.wpisz2 = tkinter.Entry(okno1, width=3)

        # ustawianie okna do bab
        text3 = tkinter.Label(okno2, text='Podaj ilosc bab ')
        self.wpisz3 = tkinter.Entry(okno2, width=3)

        przycisk1 = tkinter.Button(okno3, text='Uruchom!',
                                   command=self.wywolanie_gry)
        koniec = tkinter.Button(okno3, text='Zakoncz',
                                command=self.okno.destroy)

        text1.pack(side='left')
        self.wpisz1.pack(side='left')
        text2.pack(side='left')
        self.wpisz2.pack(side='left')
        text3.pack(side='left')
        self.wpisz3.pack(side='left')
        przycisk1.pack(side='left')
        koniec.pack(side='left')

        okno1.pack()
        okno2.pack()
        okno3.pack()

    def uruchom_okna(self):
        ''' uruchamiane sa okna widoku '''
        tkinter.mainloop()

    def sprawdzanie_zmienych(self, wysokosc, szerokosc, baby):
        ''' pobiera wartosci z okna poczatkowego
        i sprawdza czy sie zgadzaja'''
        # sprawdzanie poprawnosci pobranej liczby
        try:
            wysokosc = int(wysokosc)
            szerokosc = int(szerokosc)
            baby = int(baby)
        except ValueError:
            tkinter.messagebox.showinfo("komunikat", 'to nie jest liczba')
            self.poprawnosc = False
            return False

        try:
            if MIN_PLANSZY > wysokosc or MIN_PLANSZY > wysokosc:
                raise Wyjatek()
            elif wysokosc > MAX_PLANSZY or szerokosc > MAX_PLANSZY:
                raise Wyjatek()
        except Wyjatek:
            tkinter.messagebox.showinfo("komunikat",
                                        'podano zla wartoscc wymiary (2-15)')
            self.poprawnosc = False
            return False

        try:
            if baby < 1:
                raise Wyjatek()
            elif baby > wysokosc * szerokosc // MAX_BAB:
                raise Wyjatek()
        except Wyjatek:
            tkinter.messagebox.showinfo("komunikat",
                                        'podano za duzo lub malo bab,min to 1,'
                                        ' a max to wys*sze/3')
            self.poprawnosc = False
            return False

        self.wartosci_start = wysokosc, szerokosc, baby
        self.poprawnosc = True
        return True

    def wywolanie_gry(self):
        ''' jesli wszystkie ustawienia sa poprawne,
        uruchamiana jest klasa saper '''
        wysokosc = self.wpisz1.get()
        szerokosc = self.wpisz2.get()
        baby = self.wpisz3.get()

        if not self.sprawdzanie_zmienych(wysokosc, szerokosc, baby):
            return

        tlo = pygame.display.set_mode(WYMIARY_OKNA)
        pygame.display.set_caption('Saper')

        # wywolanie planszy
        gra = Gra(self.wartosci_start[0], self.wartosci_start[1],
                  self.wartosci_start[2])

        # petla wykonuje sie dopuki nie wylaczymy okna
        while True:
            for event in pygame.event.get():
                # wykrywanie przycisnietego klawisza

                if event.type == pygame.QUIT:
                    # pobieranie zakonczenia gry
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # pobieranie klawiszy z myszki
                    gra.ruch()

                if event.type == pygame.KEYDOWN:
                    # pobieranie klawiszy z klawiatury
                    gra.klik(event.key)

            tlo.fill((0, 0, 0))
            gra.rysuj(tlo)
            gra.koniec()
            pygame.display.flip()
