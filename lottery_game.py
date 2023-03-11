import random

def user_number_is_valid():
    """Check if user entered a number"""
    while True:
        try:
            user_number = int(input("podaj liczbe: "))
            break
        except ValueError:
            print("to nie liczba")
    return user_number

def user_list():
    """ making user list and checking the condtions"""
    result = []
    while len(result) < 6:
        number = user_number_is_valid()
        if number not in result and 0 < number <= 49:
            result.append(number)
        else:
            print("liczba nie z przedzialu, lub juz wystapila")
    return result


def lottery():
    """function that compares chosen numbers with drawn ones"""
    lottery_choice = random.sample(range(1, 49), 6)
    checked = []

    number = user_list()
    for n in lottery_choice:
        if n in number:
            checked.append(n)
    number_sorted = sorted(number)
    print(f"liczby z loterii: {lottery_choice}")
    print(f"twoje liczby: {number_sorted}")

    if len(checked) == 1:
        return f"trafiles {len(checked)} raz"
    else:
        return f"trafiles {len(checked)} razy"

if __name__ == '__main__':
    print(lottery())



