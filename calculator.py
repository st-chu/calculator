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


def is_sign_in_menu_correct(sign):
    signs = ('1', '2', '3', '4', 't', 'n')
    for item in signs:
        if sign.lower() == item:
            return True




logging.basicConfig(level=logging.DEBUG, format='%(message)s')

while True:
    type_of_calculation = input("1-Dodawanie, 2-Odejmowanie, 3-Mnożenie, 4-Dzielenie\nJakie działanie chcesz wykonać?: ")
    if is_sign_in_menu_correct(type_of_calculation) is True:
        break
    else:
        logging.warning("Coś poszło nie tak! Wybierz jeszcze raz.")


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