import pygame
from plansza import Plansza
import tkinter
import tkinter.messagebox

class Poza(Exception):
    pass

class oknoStart:
    def __init__(self):
        self.okno = tkinter.Tk()
        self.okno.title('SAPER')
        self.okno.geometry('300x200+100+100')
        self.okno1 = tkinter.Frame(self.okno)
        self.okno2 = tkinter.Frame(self.okno)
        self.okno3 = tkinter.Frame(self.okno)

        self.text1 = tkinter.Label(self.okno1,text = 'Podaj wymiary okna ')
        self.text2 = tkinter.Label(self.okno1,text = 'x')
        self.wpisz1 = tkinter.Entry(self.okno1, width=3)
        self.wpisz2 = tkinter.Entry(self.okno1, width=3)

        self.text3 = tkinter.Label(self.okno2, text='Podaj ilosc bab ')
        self.wpisz3 = tkinter.Entry(self.okno2, width=3)

        self.przycisk1 = tkinter.Button(self.okno3, text='Uruchom!', command=self.uruchomGre)
        self.koniec = tkinter.Button(self.okno3, text='Zakończ', command=self.okno.destroy)

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

        tkinter.mainloop()

    def uruchomGre(self):
        try:
            x = int(self.wpisz1.get())
            y = int(self.wpisz2.get())
            b = int(self.wpisz3.get())
        except ValueError:
            tkinter.messagebox.showinfo("komunikat", 'to nie jest liczba')
            return

        try:
            if 2 > int(self.wpisz1.get()) or 2 > int(self.wpisz2.get()):
                raise Poza()
            elif int(self.wpisz1.get()) > 15 or int(self.wpisz2.get()) > 15:
                raise Poza()
        except Poza:
            tkinter.messagebox.showinfo("komunikat", 'podano zla wartoscc wymiary (2-15)')
            return

        try:
            if 1 > int(self.wpisz3.get()):
                raise Poza()
            elif int(self.wpisz3.get()) > (int(self.wpisz1.get()) * int(self.wpisz2.get()) // 3):
                raise Poza()
        except Poza:
            tkinter.messagebox.showinfo("komunikat", 'podano za duzo lub malo bab,min to 1, a max bab to wys*sze/3')
            return

        self.uruchomPlansze(int(self.wpisz1.get()), int(self.wpisz2.get()), int(self.wpisz3.get()))

    def uruchomPlansze(self, x, y, b):
        tlo = pygame.display.set_mode((620, 680))
        pygame.display.set_caption('Saper')

        gra = Plansza(x, y, b)

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gra.ruch()
                if event.type == pygame.KEYDOWN:
                    gra.klik(event.key)

            tlo.fill((0, 0, 0))
            gra.rysuj(tlo)
            gra.koniec()
            pygame.display.flip()