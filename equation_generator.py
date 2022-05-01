import random

from kousuan_conf import SYMBOL_MINUS, SYMBOL_PLUS, get_conf


_equations = {}


def _get_key(equation):
    key = ""
    for k in equation:
        key += str(k)
    return key


def _random_picker(equations, pick_number):
    _picked = {}
    length_of_equations = len(equations)
    for i in range(pick_number):
        length_of_equations = len(equations)
        index = random.randint(0, length_of_equations-1)
        key = _get_key(equations[index])
        _picked[key] = equations[index]
        equations = equations[0:index] + \
            equations[index+1:length_of_equations]
    return _picked


def _simple_equation_generator():
    _simple_equation_config = get_conf("simple_equation")
    low_bound, up_bound, total_number = _simple_equation_config[
        "low_bound"], _simple_equation_config["up_bound"], _simple_equation_config["generate_number"]

    carry_or_abdication = _simple_equation_config["carry_or_abdication"]
    print("number of simple equations: %d" % total_number)
    print("low bound of simple equations: %d" % low_bound)
    print("up bound of simple equations: %d" % up_bound)
    print("carry or abdication for simple equations: %s\n" % carry_or_abdication)
    _simple_equations = []

    min_number = int(low_bound / 2)
    min_number = 1 if min_number == 0 else min_number
    for i in range(min_number, up_bound+1):
        for j in range(min_number, up_bound+1):
            if i+j <= up_bound and i+j >= low_bound:
                if not carry_or_abdication:
                    if int(i/10)+int(j/10) == int((i+j)/10):
                        _simple_equations.append((i, SYMBOL_PLUS, j))
                else:
                    _simple_equations.append((i, SYMBOL_PLUS, j))
            if i-j > low_bound:
                if not carry_or_abdication:
                    if int(i/10)-int(j/10) == int((i-j)/10):
                        _simple_equations.append((i, SYMBOL_MINUS, j))
                else:
                    _simple_equations.append((i, SYMBOL_MINUS, j))

    return _random_picker(_simple_equations, total_number)


def _combined_plus_equation_generator():
    _combined_plus_equation_config = get_conf("combined_plus_equation")
    low_bound, up_bound, total_number = _combined_plus_equation_config[
        "low_bound"], _combined_plus_equation_config["up_bound"], _combined_plus_equation_config["generate_number"]
    print("number of combined plus equations: %d" % total_number)
    print("low bound of combined plus equations: %d" % low_bound)
    print("up bound of combined plus equations: %d\n" % up_bound)

    min_number = int(low_bound / 3)
    min_number = 1 if min_number == 0 else min_number

    _combined_plus_equations = []
    for i in range(min_number, up_bound+1):
        for j in range(min_number, up_bound+1):
            for k in range(min_number, up_bound+1):
                if i+j+k <= up_bound and i+j+k >= low_bound:
                    _combined_plus_equations.append(
                        (i, SYMBOL_PLUS, j, SYMBOL_PLUS, k))
    return _random_picker(_combined_plus_equations, total_number)


def _combined_minus_equation_generator():
    _combined_minus_equation_config = get_conf("combined_minus_equation")
    low_bound, up_bound, total_number = _combined_minus_equation_config[
        "low_bound"], _combined_minus_equation_config["up_bound"], _combined_minus_equation_config["generate_number"]
    print("number of combined minus equations: %d" % total_number)
    print("low bound of combined minus equations: %d" % low_bound)
    print("up bound of combined minus equations: %d\n" % up_bound)

    min_number = int(low_bound / 3)
    min_number = 1 if min_number == 0 else min_number

    _combined_minus_equations = []
    for i in range(low_bound+2, up_bound+1):
        for j in range(min_number, up_bound+1):
            if i - j < 0:
                continue
            for k in range(min_number, up_bound+1):
                if i - j - k > low_bound:
                    _combined_minus_equations.append(
                        (i, SYMBOL_MINUS, j, SYMBOL_MINUS, k))
    return _random_picker(_combined_minus_equations, total_number)


def _mixed_equation_generator():
    _mixed_equation_config = get_conf("mixed_equation")
    low_bound, up_bound, total_number = _mixed_equation_config[
        "low_bound"], _mixed_equation_config["up_bound"], _mixed_equation_config["generate_number"]
    print("number of mixed equations: %d" % total_number)
    print("low bound of mixed equations: %d" % low_bound)
    print("up bound of mixed equations: %d\n" % up_bound)

    min_number = int(low_bound / 3)
    min_number = 1 if min_number == 0 else min_number

    _mixed_equations = []
    for i in range(min_number, up_bound+1):
        for j in range(min_number, up_bound+1):
            for k in range(min_number, up_bound+1):
                if i + j <= up_bound and i + j - k > low_bound and i + j - k <= up_bound:
                    _mixed_equations.append(
                        (i, SYMBOL_PLUS, j, SYMBOL_MINUS, k))
                if i - j > 0 and i - j + k <= up_bound and i - j + k >= low_bound:
                    _mixed_equations.append(
                        (i, SYMBOL_MINUS, j, SYMBOL_PLUS, k))
    return _random_picker(_mixed_equations, total_number)


def generate():
    global _equations
    _equations = {}

    _equations.update(_simple_equation_generator())

    _equations.update(_combined_plus_equation_generator())

    _equations.update(_combined_minus_equation_generator())

    _equations.update(_mixed_equation_generator())

    return _equations
