# Saper
##### Projekt z JS 
Mój projekt saper składa się głównie z dwóch okien, okna startu gry i okna gry. Pierwsze okno ma za zadanie pobrać dane początkowe i sprawdzić czy są zgodne jeśli tak to uruchamiane jest drugie okno z gra. Jest też klasa testująca okno start.

Okno startu jest to klasa która jest napisana na trikner, błędy są wyłapywane przez klasę z wyjątkami.

Okno gry to klasa napisana na pygame, pobiera ona pliki png stworzone przeze mnie do graficznego interfejsu. W grze gracz steruje myszka używając dwóch klawiszy,  funkcja ruch wyłapuje kliknięcia i wywołuje odpowiednia funkcje wybuchu bab, odkrycia kafelka lub odkrycia wielu pustych elementów wokół siebie, jest też funkcja rysowania wszystkich elementów graficznych przycisków, pola wygrana/przegrana, reset i licznik. Funkcjonuje też funkcja wyłapująca kod 'xyzzy'.

Klasa testująca sprawdza głównie czy klasa startu poprawnie sprawdziła początkowe wartości.

#### Klasy
[Gra](https://github.com/FilipK-PK/Saper/blob/0413525c9a5175226af5267d6efd3a115a38c87a/gra.py#L80)

[Plansza](https://github.com/FilipK-PK/Saper/blob/0413525c9a5175226af5267d6efd3a115a38c87a/gra.py#L65)
