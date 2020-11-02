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


def is_int(value):
    try:
        int(value)
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
            a = a.replace(',', '.')
            if is_number(a) is True:
                a = float(a)
                break
            else:
                print('-' * 70)
                logging.warning("Wpisana wartość nie jest liczbą, spróbuj jeszcze raz.")
                print('-' * 70)
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
    while True:
        type_of_calculation = input("\n1-Dodawanie, 2-Odejmowanie, 3-Mnożenie, 4-Dzielenie, Q/q-Wyjście\nJakie działanie chcesz wykonać?: ")
        if is_sign_in_menu_correct(type_of_calculation) is True:
            break
        else:
            print('-' * 70)
            logging.warning("Coś poszło nie tak! Wybierz jeszcze raz.")
            print('-' * 70)
    if type_of_calculation == '1':
        while True:
            _range = input("\nIle liczb chcesz ze sobą dodać?: ")
            if is_int(_range) is not True:
                print('-' * 70)
                logging.warning("Wpisana wartość nie jest liczbą całkowitą, spróbuj jeszcze raz.")
                print('-' * 70)
            else:
                _range = int(_range)
                if _range < 2:
                    print('-' * 70)
                    logging.warning("Liczb musi być więcej niż jedna!")
                    print('-' * 70)
                else:
                    break
        numbers = num_lst(_range)
        print('-' * 70)
        logging.info("Przeprowadzone działanie: " + num_str(numbers, '+'))
        print(f'Wynik działania: {add(numbers)}')
        print('-' * 70)
    if type_of_calculation == '2':
        numbers = num_lst()
        print('-' * 70)
        logging.info("Przeprowadzone działanie: " + num_str(numbers, '-'))
        print(f'Wynik działania: {sub(numbers)}')
        print('-' * 70)
    if type_of_calculation == '3':
        while True:
            _range = input("\nIle liczb chcesz ze sobą pomnożyć?: ")
            if is_int(_range) is not True:
                print('-' * 70)
                logging.warning("Wpisana wartość nie jest liczbą całkowitą, spróbuj jeszcze raz.")
                print('-' * 70)
            else:
                _range = int(_range)
                if _range < 2:
                    print('-' * 70)
                    logging.warning("Liczb musi być więcej niż jedna!")
                    print('-' * 70)
                else:
                    break
        numbers = num_lst(_range)
        print('-' * 70)
        logging.info("Przeprowadzone działanie: " + num_str(numbers, '*'))
        print(f'Wynik działania: {mul(numbers)}')
        print('-' * 70)
    if type_of_calculation == '4':
        numbers = num_lst()
        print('-' * 70)
        logging.info("Przeprowadzone działanie: " + num_str(numbers, '/'))
        print(f'Wynik działania: {div(numbers)}')
        print('-' * 70)
    if type_of_calculation.lower() == 'q':
        print("\nDzięki za uwagę.\n")
        break