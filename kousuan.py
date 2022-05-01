

import argparse

from equation_generator import generate
from equation_writor import write_to_file
from kousuan_conf import BATCH_COUNT, load_conf, get_conf


def main():
    parser = argparse.ArgumentParser("口算参数配置")
    parser.add_argument("-f", "--config_file", default="./kousuan.conf")

    args = parser.parse_args()
    config_file = args.config_file
    load_conf(config_file)

    batch_count = get_conf(BATCH_COUNT, 1)

    for i in range(int(batch_count)):
        equations = generate()
        #for k in equations:
        #    print(k)
        write_to_file(equations)


if __name__ == "__main__":
    main()
