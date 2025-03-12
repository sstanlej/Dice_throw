PIPR Projekt 1 - mały nr 12
Symulator rzutu kostką
Stanisław Liszewski

Opis programu:
Program jest aplikacją konsolową pozwalającą na symulację rzutu różnymi rodzajami kostek z różną ilością ścianek. Po uruchomieniu programu w konsoli wyświetli się komunikat z prośbą o podanie liczby ścianek kostki. Po wprowadzeniu liczby ścianek (dodatniej) wyświetli się proste menu z trzema opcjami:

0. Exit
1. Throw
2. Input number of sides

Wybór opcji odbywa się również poprzez konsolę.
Wybór 0 spowoduje zakończenie działania programu. 
Wybór 1 spowoduje "rzut kostką", czyli wylosowanie liczby z zakresu od 1 do podanej wcześniej liczby ścianek oraz wyświetlenie wyniku i ponowne wyświetlenie menu, co umożliwi ponowny rzut.
Wybór 2 spowoduje powrót do początku programu, czyli ponownie wyświetli się prośba o podanie liczby ścianek kostki a następnie menu.

Program składa się z następujących funkcji:
cls() - czyszczenie zawartości konsoli zarówno na komputerach z systemem windows oraz linux
input_sides() - prośba o podanie ilości ścianek (dodatniej liczby całkowitej) i sprawdzenie poprawności wpisanej danej
input_operation() - prośba o podanie opcji z menu (liczba od 0 do 1) i sprawdzenie poprawności
throw(sides) - wylosowanie liczby od 1 do *sides*, wyświetlenie wylosowanej liczby
menu(sides) - wyświetlenie wybranej liczby ścianek i opcji, możliwość wybrania opcji
main() - początek programu, wywołanie input_sides() i menu()
