

import argparse

from equation_generator import generate
from equation_writor import write_to_file
from kousuan_conf import NUMBER_OF_EQUATIONS, UPPER_BOUND_OF_NUMBER, BATCH_COUNT, load_conf, get_conf


def main():
    parser = argparse.ArgumentParser("口算参数配置")
    parser.add_argument("-f", "--config_file", default="./kousuan.conf")

    args = parser.parse_args()
    config_file = args.config_file
    load_conf(config_file)

    number_of_equations = get_conf(NUMBER_OF_EQUATIONS, 100)
    upper_bound_of_number = get_conf(UPPER_BOUND_OF_NUMBER, 20)
    batch_count = get_conf(BATCH_COUNT, 1)

    print(int(batch_count))
    for i in range(int(batch_count)):
        equations = generate(int(upper_bound_of_number), int(number_of_equations))
        write_to_file(equations)


if __name__ == "__main__":
    main()
