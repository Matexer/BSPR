PL
# Badanie Stałych Paliw Rakietowych v1.1
Program umożliwia opracowanie wyników badań stałych paliw rakietowych, w celu wyznaczenia impulsu jednostkowego paliwa oraz charakterystyk A i n potęgowego prawa szybkości spalania. Stanowił zadanie do realizacji pracy dyplomowej na studiach I stopnia, na kierunku mechatronika.

Wersja dla systemu Windows, niewymagająca instalacji dodatkowych składników (Python etc.).
https://drive.google.com/file/d/1-S0pdQ1UP_KuVMmwkPsVQdOwsqRK_tu7/view?usp=sharing

Użytkownik posiada możliwość korekty importowanych przebiegów ciśnienia i ciągu, polegającej na podaniu wartości współczynnika skali i zaznaczenia na wykresie odpowiednio:
- czasu rozpoczęcia pracy silnika,
- czasu końca spalania paliwa,
- czasu końca pracy silnika rakietowego.

Przykład pliku do importu danych pomiarowych znajduje się w folderze data_samples. Jest to jednoczesny pomair ciśnienia (lewa kolumna) i ciągu (prawa kolumna) bez przemnożenia przez współczynnik skali.

Możliwy jest eksport pozyskanych wyników do pliku o formacie CSV, a także wykresów do pliku o fromacie PNG.

Wygląd GUI (Linux Mint 20)

1.Lista pomiarów

![Lista pomiarówt](/../master/screens/fuels_list.png?raw=true "Lista pomiarów")

2. Dodawanie pomiaru

![Dodawanie pomiaru](/../master/screens/adding_survey.png?raw=true "Dodawanie pomiaru")

3. Konfiguracja obliczeń

![Konfiguracja obliczeń](/../master/screens/imp_config.png?raw=true "Konfiguracja obliczeń")

4. Wyniki obliczeń

![Wyniki obliczeń](/../master/screens/An_output2.png?raw=true "Wyniki obliczeń")

![Wyniki obliczeń](/../master/screens/An_output.png?raw=true "Wyniki obliczeń")

