def guess_number():
    """
       Ten program to gra w zgadywanie liczby, w której komputer próbuje odgadnąć liczbę
       wymyśloną przez użytkownika z zakresu od 1 do 1000. Użytkownik udziela odpowiedzi,
       czy komputerowa propozycja jest "za duża", "za mała" czy "zgadłeś".
       Komputer wykorzystuje algorytm wyszukiwania binarnego, aby zgadnąć liczbę w maksymalnie 10 próbach,pod warunkiem, że użytkownik gra uczciwie.
    """
    print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max 10 próbach")
    print(input("Naciśnij enter aby kontynuować"))

    max_value = 1000
    min_value = 0
    attempts = 0

    while attempts < 10:
        guess = (min_value + max_value) // 2
        print(f"Zgaduję: {guess}")

        answer = input("Wpisz: 'za dużo', 'za mało', 'zgadłeś': ").lower()
        if answer == "zgadłeś":
            print("Wygrałem")
            return
        elif answer == "za dużo":
           max_value = guess
        elif answer == "za mało":
            min_value = guess
        else:
            print("Nie oszukuj")
            continue
        attempts += 1

if __name__ == "__main__":
    guess_number()
    