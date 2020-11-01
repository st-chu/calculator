import logging


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


logging.basicConfig(level=logging.DEBUG, format='%(message)s')
type_of_calculation = input("1-Dodawanie, 2-Odejmowanie, 3-Mnożenie, 4-Dzielenie\nJakie działanie chcesz wykonać?: ")

while True:
    number_a = input("Podaj pierwszą liczbę: ")
    if is_number(number_a) is True:
        number_a = float(number_a)
        break
    else:
        logging.warning("Wpisana wartość nie jest liczbą, spróbuj jeszcze raz.")

while True:
    number_b = input("Podaj drugą liczbę: ")
    if is_number(number_b) is True:
        number_b = float(number_b)
        break
    else:
        logging.warning("Wpisana wartość nie jest liczbą, spróbuj jeszcze raz.")

if type_of_calculation == '1':
    logging.info("Dodaję %.2f do %.2f" % (number_a, number_b))
    print(f'Wynik dodawania: {add(number_a,number_b)}')
if type_of_calculation == '2':
    logging.info("Odejmuję %.2f od %.2f" % (number_a, number_b))
    print(f'Wynik odejmowania: {sub(number_a, number_b)}')
if type_of_calculation == '3':
    logging.info("Mnożę %.2f przez %.2f" % (number_a, number_b))
    print(f'Wynik mnożenia: {mul(number_a, number_b)}')
if type_of_calculation == '4':
    logging.info("Dzielę %.2f przez %.2f" % (number_a, number_b))
    print(f'Wynik mnożenia: {div(number_a, number_b)}')