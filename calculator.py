import logging


def add(numbers_list):
    _sum = 0
    for number in numbers_list:
        _sum += number
    return _sum


def sub(number_list):
    _sub = number_list[0]
    for number in range(1, len(number_list)):
        _sub -= number_list[number]
    return _sub


def mul(number_list):
    _mul = number_list[0]
    for number in range(1, len(number_list)):
        _mul *= number_list[number]
    return _mul


def div(number_list):
    _div = number_list[0]
    for number in range(1, len(number_list)):
        _div /= number_list[number]
    return _div


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_sign_in_menu_correct(sign):
    signs = ('1', '2', '3', '4', 'q')
    for item in signs:
        if sign.lower() == item:
            return True


def num_lst(_range=2):
    number_list = []
    for number in range(1, _range + 1):
        while True:
            a = input("Podaj liczbę %d: " % number)
            if is_number(a) is True:
                a = float(a)
                break
            else:
                logging.warning("\nWpisana wartość nie jest liczbą, spróbuj jeszcze raz.")
        number_list.append(a)
    return number_list


def num_str(number_list, sign):
    sentence = ''
    for number in number_list:
        sentence += str(number) + ' ' + str(sign) + ' '
    sentence = sentence[:-2]
    return sentence


logging.basicConfig(level=logging.DEBUG, format='%(message)s')


while True:
    type_of_calculation = input("1-Dodawanie, 2-Odejmowanie, 3-Mnożenie, 4-Dzielenie, Q-Wyjście\nJakie działanie chcesz wykonać?: ")
    if is_sign_in_menu_correct(type_of_calculation) is True:
        break
    else:
        logging.warning("Coś poszło nie tak! Wybierz jeszcze raz.")


if type_of_calculation == '1':
    _range = int(input("Ile liczb chcesz ze sobą dodać?: "))
    numbers = num_lst(_range)
    logging.info("Przeprowadzone działanie: " + num_str(numbers, '+'))
    print(f'Wynik działania: {add(numbers)}')
if type_of_calculation == '2':
    numbers = num_lst()
    logging.info("Przeprowadzone działanie: " + num_str(numbers, '-'))
    print(f'Wynik działania: {sub(numbers)}')
if type_of_calculation == '3':
    _range = int(input("Ile liczb chcesz ze sobą pomnożyć?: "))
    numbers = num_lst(_range)
    logging.info("Przeprowadzone działanie: " + num_str(numbers, '*'))
    print(f'Wynik działania: {mul(numbers)}')
if type_of_calculation == '4':
    numbers = num_lst()
    logging.info("Przeprowadzone działanie: " + num_str(numbers, '/'))
    print(f'Wynik działania: {div(numbers)}')