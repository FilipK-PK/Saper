import pygame
import tkinter
import tkinter.messagebox
from gra import Gra

WYMIARY_OKNA = (620,680)
MAX_PLANSZY = 15
MIN_PLANSZY = 2
MAX_BAB = 3 # ilosci przyciskow/MAX_BAB to maksymalna liczba bab

#klasam wyjatkow
class Poza(Exception):
    pass

class OknoStart:
    def __init__(self):
        self.wartosciStart = (2,2,1)
        self.poprawnosc = False
        self.okno = tkinter.Tk()
        self.okno.title('SAPER')
        self.okno.geometry('300x200+100+100')
        self.okno1 = tkinter.Frame(self.okno)
        self.okno2 = tkinter.Frame(self.okno)
        self.okno3 = tkinter.Frame(self.okno)

        #ustawianie okien do wymiarow
        self.text1 = tkinter.Label(self.okno1,text = 'Podaj wymiary okna ')
        self.text2 = tkinter.Label(self.okno1,text = 'x')
        self.wpisz1 = tkinter.Entry(self.okno1, width=3)
        self.wpisz2 = tkinter.Entry(self.okno1, width=3)

        # ustawianie okna do bab
        self.text3 = tkinter.Label(self.okno2, text='Podaj ilosc bab ')
        self.wpisz3 = tkinter.Entry(self.okno2, width=3)

        self.przycisk1 = tkinter.Button(self.okno3, text='Uruchom!', command=self.sprawdzanie_Wartosci_Poczatkowych)
        self.koniec = tkinter.Button(self.okno3, text='Zakończ', command=self.okno.destroy)

        #ustawianie polorzenia elementow
        self.text1.pack(side='left')
        self.wpisz1.pack(side='left')
        self.text2.pack(side='left')
        self.wpisz2.pack(side='left')
        self.text3.pack(side='left')
        self.wpisz3.pack(side='left')
        self.przycisk1.pack(side ='left')
        self.koniec.pack(side='left')

        self.okno1.pack()
        self.okno2.pack()
        self.okno3.pack()

        self.trinker()

    def trinker(self):
        tkinter.mainloop()

    def sprawdzanie_Wartosci_Poczatkowych(self):
        #sprawdzanie poprawnosci pobranej liczby
        try:
            wysokosc = int(self.wpisz1.get())
            szerokosc = int(self.wpisz2.get())
            baby = int(self.wpisz3.get())
        except ValueError:
            tkinter.messagebox.showinfo("komunikat", 'to nie jest liczba')
            self.poprawnosc = False
            return False

        try:
            if MIN_PLANSZY > wysokosc or MIN_PLANSZY > wysokosc:
                raise Poza()
            elif wysokosc > MAX_PLANSZY or szerokosc > MAX_PLANSZY:
                raise Poza()
        except Poza:
            tkinter.messagebox.showinfo("komunikat", 'podano zla wartoscc wymiary (2-15)')
            self.poprawnosc = False
            return False

        try:
            if 1 > baby:
                raise Poza()
            elif baby > wysokosc * szerokosc // MAX_BAB:
                raise Poza()
        except Poza:
            tkinter.messagebox.showinfo("komunikat", 'podano za duzo lub malo bab,min to 1, a max bab to wys*sze/3')
            self.poprawnosc = False
            return False

        self.Wartosci_Start = (wysokosc, szerokosc, baby)

        self.poprawnosc = True

        self.wywolanie_gry(wysokosc, szerokosc, baby)
        return True

    def wywolanie_gry(self, wysokosc, szerokosc, baby):
        tlo = pygame.display.set_mode(WYMIARY_OKNA)
        pygame.display.set_caption('Saper')

        # wywołanie planszy
        gra = Gra(wysokosc, szerokosc, baby)

        # petla wykonuje sie dopuki nie wyłaczymy okna
        while True:
            for event in pygame.event.get():  # wykrywanie przycisnietego klawisza
                if event.type == pygame.QUIT:  # pobieranie zakonczenia gry
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:  # pobieranie klawiszy z myszki
                    gra.ruch()
                if event.type == pygame.KEYDOWN:  # pobieranie klawiszy z klawiatury
                    gra.klik(event.key)

            tlo.fill((0, 0, 0))
            gra.rysuj(tlo)
            gra.koniec()
            pygame.display.flip()

