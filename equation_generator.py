import random

from kousuan_conf import NUMBER_OF_COMBINED_MINUS_EQUATIONS, NUMBER_OF_COMBINED_PLUS_EQUATIONS, NUMBER_OF_MIXED_EQUATIONS, get_conf


SYMBOL_PLUS = "+"
SYMBOL_MINUS = "-"


_equations = {}


def _number_generator(lower_bound, upper_bound):
    if upper_bound == 1:
        return 1
    return random.randint(lower_bound, upper_bound - 1)


def _symbol_generator():
    i = random.randint(1, 2)
    if i == 1:
        return SYMBOL_PLUS
    else:
        return SYMBOL_MINUS


def _simple_equation_generator(num_limit):
    first_number = _number_generator(1, num_limit)
    symbol = _symbol_generator()
    second_number = 0
    if symbol == SYMBOL_PLUS:
        second_number = _number_generator(1, num_limit - first_number)
    else:
        second_number = _number_generator(1, first_number)

    return (first_number, symbol, second_number)


def _combined_plus_equation_generator(num_limit):
    first_number = _number_generator(1, num_limit - 1)
    second_number = _number_generator(1, num_limit - first_number - 1)
    third_number = _number_generator(
        1, num_limit - first_number - second_number)
    return (first_number, SYMBOL_PLUS, second_number, SYMBOL_PLUS, third_number)


def _combined_minus_equation_generator(num_limit):
    first_number = _number_generator(2, num_limit)
    second_number = _number_generator(1, first_number - 1)
    third_number = _number_generator(1, first_number - second_number)
    return (first_number, SYMBOL_MINUS, second_number, SYMBOL_MINUS, third_number)


def _mixed_equation_generator(num_limit):
    first_number = _number_generator(1, num_limit)
    first_symbol = _symbol_generator()
    second_symbol, second_number, third_number = "", 0, 0
    if first_symbol == SYMBOL_PLUS:
        second_number = _number_generator(1, num_limit - first_number)
        second_symbol = SYMBOL_MINUS
    else:
        second_number = _number_generator(1, first_number)
        second_symbol = SYMBOL_PLUS

    if second_symbol == SYMBOL_PLUS:
        third_number = _number_generator(
            1, num_limit - (first_number - second_number))
    else:
        third_number = _number_generator(1, first_number + second_number)

    return (first_number, first_symbol, second_number, second_symbol, third_number)


def validate(num_limit, equation_number):
    total = 0
    for i in range(num_limit+1):
        total += (num_limit - i + 1) + i
    print("total possible equation number: %d" % total)
    return total >= equation_number


def generate(upper_bound_of_number, equation_number):
    if not validate(upper_bound_of_number, equation_number):
        raise Exception("required equation number %d is larger than total possible equation number when num limit is %d" % (
            upper_bound_of_number, equation_number))

    number_of_combined_plus_equations = int(get_conf(NUMBER_OF_COMBINED_PLUS_EQUATIONS, 0))
    number_of_combined_minus_equations = int(get_conf(NUMBER_OF_COMBINED_MINUS_EQUATIONS, 0))
    number_of_mixed_equations = int(get_conf(NUMBER_OF_MIXED_EQUATIONS, 0))
    number_of_simple_equations = equation_number
    - number_of_combined_plus_equations
    - number_of_combined_minus_equations
    - number_of_mixed_equations

    print(number_of_combined_plus_equations)
    print(number_of_combined_minus_equations)
    print(number_of_mixed_equations)
    print(number_of_simple_equations)

    if number_of_simple_equations < 0:
        required_equation_number = number_of_combined_plus_equations + number_of_mixed_equations + number_of_combined_minus_equations
        raise Exception("required equation number %d is larger than total equation number %d" % (
            required_equation_number, equation_number))

    for i in range(number_of_simple_equations):
        while True:
            if not isDup(_simple_equation_generator(upper_bound_of_number)):
                break

    for i in range(number_of_combined_plus_equations):
        while True:
            if not isDup(_combined_plus_equation_generator(upper_bound_of_number)):
                break

    for i in range(number_of_combined_minus_equations):
        while True:
            if not isDup(_combined_minus_equation_generator(upper_bound_of_number)):
                break

    for i in range(number_of_mixed_equations):
        while True:
            if not isDup(_mixed_equation_generator(upper_bound_of_number)):
                break

    global _equations
    return _equations


def isDup(equation):
    key = ""
    for s in equation:
        key += str(s)

    if key in _equations:
        return True
    _equations[key] = equation
    return False
