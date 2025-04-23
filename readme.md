# Aplikacja do rzucania kostką
Autor: Stanisław Liszewski

To prosta aplikacja okienkowa napisana w Pythonie z wykorzystaniem biblioteki tkinter. Umożliwia użytkownikowi wybór liczby ścianek kostki oraz wykonanie animowanego rzutu. Program został wzbogacony o animację oraz obsługę klawisza Enter.

## Funkcje programu

- Wybór liczby ścianek kostki (np. 6, 20, 100 itp.)
- Rzut kostką z animacją (ludzik rzucający kostką)
- Obsługa myszki i klawisza Enter
- Zabezpieczenie przed ponownym rzutem w trakcie animacji
- Wyświetlanie wyniku na końcowej grafice

## Interfejs użytkownika

- **Pole tekstowe** – służy do wpisania liczby ścianek
- **Przycisk `Throw Dice`** – wykonuje rzut kostką
- **Enter** – zatwierdza wpisaną liczbę lub rzuca kostką

## Główne funkcje aplikacji

- `throw_dice()` – uruchamia animację i losuje wynik
- `set_sides()` – ustawia liczbę ścianek kostki
- `show_previous_results()` - pokazuje ostatnie wyniki rzutu oraz statystyki

## Obrazy

Aplikacja korzysta z 4 obrazków w folderze z programem. Na ostatnim obrazku pojawia się wynik rzutu.
