import pygame
import os

#dodaje grafike dla przyciskow
l0 = pygame.image.load(os.path.join('png','0.png'))
l1 = pygame.image.load(os.path.join('png','1.png'))
l2 = pygame.image.load(os.path.join('png','2.png'))
l3 = pygame.image.load(os.path.join('png','3.png'))
l4 = pygame.image.load(os.path.join('png','4.png'))
l5 = pygame.image.load(os.path.join('png','5.png'))
l6 = pygame.image.load(os.path.join('png','6.png'))
l7 = pygame.image.load(os.path.join('png','7.png'))
l8 = pygame.image.load(os.path.join('png','8.png'))

lp = pygame.image.load(os.path.join('png','p.png'))
lr = pygame.image.load(os.path.join('png','r.png'))
lpp = pygame.image.load(os.path.join('png','bp.png'))
lf = pygame.image.load(os.path.join('png','f.png'))
lb = pygame.image.load(os.path.join('png','b.png'))
lbw = pygame.image.load(os.path.join('png','bw.png'))
lbr = pygame.image.load(os.path.join('png','br.png'))
lz = pygame.image.load(os.path.join('png','z.png'))
lw = pygame.image.load(os.path.join('png','w.png'))
lk = pygame.image.load(os.path.join('png','k.png'))

ln0 = pygame.image.load(os.path.join('png','n0.png'))
ln1 = pygame.image.load(os.path.join('png','n1.png'))
ln2 = pygame.image.load(os.path.join('png','n2.png'))
ln3 = pygame.image.load(os.path.join('png','n3.png'))
ln4 = pygame.image.load(os.path.join('png','n4.png'))
ln5 = pygame.image.load(os.path.join('png','n5.png'))
ln6 = pygame.image.load(os.path.join('png','n6.png'))
ln7 = pygame.image.load(os.path.join('png','n7.png'))
ln8 = pygame.image.load(os.path.join('png','n8.png'))
ln9 = pygame.image.load(os.path.join('png','n9.png'))
lnm = pygame.image.load(os.path.join('png','n-.png'))
lnn = pygame.image.load(os.path.join('png','nn.png'))

class Grafika():
    def __init__(self, s, w):
        self.w = w
        self.s = s
        self.ox = int((600 - s * 40) / 2) + 10
        self.oy = 70
        self.Macierz = [[(0, 0) for i in range(s)] for j in range(w)]

    def rysFlagi(self,tlo):
        m = (ln0, ln1, ln2, ln3, ln4, ln5, ln6, ln7, ln8, ln9)
        x = abs(self.liczbikB)

        if x < 100:
            tlo.blit(lnn, (20, 10))
        else:
            tlo.blit(m[x//100], (20, 10))
        x = x % 100

        if x < 10:
            tlo.blit(lnn, (50, 10))
        else:
            tlo.blit(m[x//10], (50, 10))
        x = x % 10

        tlo.blit(m[x], (80, 10))

        if self.liczbikB < 0:
            if self.liczbikB > -10:
                tlo.blit(lnm, (50, 10))
            elif self.liczbikB > -100:
                tlo.blit(lnm, (20, 10))

    def rysuj(self, surface):
        self.rysFlagi(surface)
        surface.blit(lr, (215,10))
    
        # wyswietlanie wygranej/przegranej
        if self.win:
            surface.blit(lw, (440,5))
        if self.end:
            surface.blit(lk, (440,5))
        
        #rozmieszczam odpowiednie ikonki w odpowiednim mniejscu
        for y in range(len(self.Macierz)):
            for x in range(len(self.Macierz[y])):
                if self.Macierz[y][x][1] == 1:
                    if self.Macierz[y][x][0] == 0:
                        surface.blit(lp, (self.ox + x * 40, self.oy + y * 40))
                    elif self.Macierz[y][x][0] == 'x':
                        surface.blit(lbw, (self.ox + x * 40, self.oy + y * 40))
                    elif self.Macierz[y][x][0] == 1:
                        surface.blit(l1, (self.ox + x * 40, self.oy + y * 40))
                    elif self.Macierz[y][x][0] == 2:
                        surface.blit(l2, (self.ox + x * 40, self.oy + y * 40))
                    elif self.Macierz[y][x][0] == 3:
                        surface.blit(l3, (self.ox + x * 40, self.oy + y * 40))
                    elif self.Macierz[y][x][0] == 4:
                        surface.blit(l4, (self.ox + x * 40, self.oy + y * 40))
                    elif self.Macierz[y][x][0] == 5:
                        surface.blit(l5, (self.ox + x * 40, self.oy + y * 40))
                    elif self.Macierz[y][x][0] == 6:
                        surface.blit(l6, (self.ox + x * 40, self.oy + y * 40))
                    elif self.Macierz[y][x][0] == 7:
                        surface.blit(l7, (self.ox + x * 40, self.oy + y * 40))
                    elif self.Macierz[y][x][0] == 8:
                        surface.blit(l8, (self.ox + x * 40, self.oy + y * 40))
                    elif self.Macierz[y][x][0] == 'b':
                        surface.blit(lb, (self.ox + x * 40, self.oy + y * 40))
                    elif self.Macierz[y][x][0] == 'bp':
                        surface.blit(lpp, (self.ox + x * 40, self.oy + y * 40))
                elif self.Macierz[y][x][1] == 0:
                    if self.Macierz[y][x][0] == 'x' and self.faul:
                        surface.blit(lbr, (self.ox + x * 40, self.oy + y * 40))
                    else:
                        surface.blit(l0, (self.ox + x * 40, self.oy + y * 40))
                elif self.Macierz[y][x][1] == 2:
                    surface.blit(lf, (self.ox + x * 40, self.oy + y * 40))
                elif self.Macierz[y][x][1] == 3:
                    surface.blit(lz, (self.ox + x * 40, self.oy + y * 40))

    def wyswietl_g(self):
        for i in self.Macierz:
            print(i)
        print()
