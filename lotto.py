# Napisz program, który:
#
# zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
# czy wprowadzony ciąg znaków jest poprawną liczbą,
# czy użytkownik nie wpisał tej liczby już poprzednio,
# czy liczba należy do zakresu 1-49,
# po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
# wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
# poinformuje gracza, ile liczb trafił.
import random


def check(num):  # funkcja sprawdzająca liczby użytkownika
    if num < 1 or num > 49:
        print("Wrong number - please give a number form 1 to 49")
    elif num in lotto_user:
        print("The number is already on the list, give another")
    else:
        lotto_user.append(num)
        print(f"{lotto_user}")
    return lotto_user


def check_c(num_c):  # funkcja sprawdzająca liczby losowane
    if num_c in lotto_comp:
        print("The number is already on the list, give another")
    else:
        lotto_comp.append(num_c)
    return lotto_comp


lotto_user = []
lotto_comp = []
num = int()
num_c = int()

# moduł pobrania liczb użytkownika
while len(lotto_user) < 6:
    try:
        num = int(input("Enter number: "))
        n1 = check(num)
    except:
        print("It's not a number")
        continue


# moduł losowanie lotto
while len(lotto_comp) < 6:
        num_c = random.randint(1, 49)
        n2 = check_c(num_c)

# wyniki
lotto_user.sort()
lotto_comp.sort()
print()
print("--------------------------------------")
print()
print(f"User choice {lotto_user}")
print()
print("--------------------------------------")
print(f"Lotto choice {lotto_comp}")
print()
# trafienia
hits = []
for n in lotto_user:  # iteracja pierwszej listy
    for n1 in lotto_comp:  # iteracja drugiej listy
        if n == n1:  # porównanie elementów
            hits.append(n)

print(f"You hit {len(hits)} number(s) - {hits}")
if len(hits) >= 3:
    print("You win!")
else:
    print("Maybe you win next time.")
