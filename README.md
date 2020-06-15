# Saper
##### Projekt z JS 
Mój projekt saper składa się głównie z dwóch okien, okna startu gry i okna gry. Pierwsze okno ma za zadanie pobrać dane początkowe i sprawdzić czy są zgodne jeśli tak to uruchamiane jest drugie okno z gra. Jest też klasa testująca okno start.

Okno startu jest to klasa która jest napisana na trikner, błędy są wyłapywane przez klasę z wyjątkami.

Okno gry to klasa napisana na pygame, pobiera ona pliki png stworzone przeze mnie do graficznego interfejsu. W grze gracz steruje myszka używając dwóch klawiszy,  funkcja ruch wyłapuje kliknięcia i wywołuje odpowiednia funkcje wybuchu bab, odkrycia kafelka lub odkrycia wielu pustych elementów wokół siebie, jest też funkcja rysowania wszystkich elementów graficznych przycisków, pola wygrana/przegrana, reset i licznik. Funkcjonuje też funkcja wyłapująca kod 'xyzzy'.

Klasa testująca sprawdza głównie czy klasa startu poprawnie sprawdziła początkowe wartości.

#### Klasy
[Gra](https://github.com/FilipK-PK/Saper/blob/0413525c9a5175226af5267d6efd3a115a38c87a/gra.py#L80)  
[Plansza](https://github.com/FilipK-PK/Saper/blob/0413525c9a5175226af5267d6efd3a115a38c87a/gra.py#L65)  
[Klasa Wyjatków](https://github.com/FilipK-PK/Saper/blob/dabd49dd9e6321a867bbea224b15a6effff567c9/okno_start.py#L14)  
[Okno start](https://github.com/FilipK-PK/Saper/blob/dabd49dd9e6321a867bbea224b15a6effff567c9/okno_start.py#L19)

#### Wyjatki
[1](https://github.com/FilipK-PK/Saper/blob/dabd49dd9e6321a867bbea224b15a6effff567c9/okno_start.py#L67)  
[2](https://github.com/FilipK-PK/Saper/blob/dabd49dd9e6321a867bbea224b15a6effff567c9/okno_start.py#L76)  
[3](https://github.com/FilipK-PK/Saper/blob/dabd49dd9e6321a867bbea224b15a6effff567c9/okno_start.py#L87)  

#### List comprehensions
[LC](https://github.com/FilipK-PK/Saper/blob/0413525c9a5175226af5267d6efd3a115a38c87a/gra.py#L80)  
