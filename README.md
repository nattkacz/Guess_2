# Guess_2

# Opis programu
Ten program jest grą, w której komputer próbuje zgadnąć liczbę wybraną przez użytkownika z zakresu od 1 do 1000. Użytkownik myśli o liczbie, a komputer dokonuje kolejnych zgadywań, przy czym użytkownik udziela odpowiedzi, czy liczba jest „za dużo”, „za mało”, czy „zgadłeś”. Program wykorzystuje strategię binarnego przeszukiwania, aby zoptymalizować liczbę prób i zgadnąć liczbę w maksymalnie 10 krokach.

## Sposób działania
### Początek: Program prosi użytkownika o pomyślenie liczby z zakresu 0–1000.
### Zgadywanie: Komputer wykonuje zgadywanie, korzystając z wartości środkowej bieżącego zakresu (między minimalną a maksymalną wartością).

## Odpowiedź użytkownika:
### Jeśli użytkownik odpowie „zgadłeś”, program kończy się sukcesem.
Jeśli odpowie „za dużo”, komputer zmniejsza maksymalny zakres o zgadywaną liczbę.
Jeśli odpowie „za mało”, komputer zwiększa minimalny zakres o zgadywaną liczbę.
Kontrola oszustwa: Jeśli użytkownik poda nieprawidłową odpowiedź, program zwraca komunikat „Nie oszukuj!”.
Limit prób: Komputer ma maksymalnie 10 prób, aby zgadnąć liczbę. Jeśli się nie uda, program informuje, że limit prób został wyczerpany.

## Funkcje
guess_number(): Główna funkcja realizująca całą logikę gry, w tym zgadywanie liczby oraz interpretację odpowiedzi użytkownika.
