

import configparser
from stat import FILE_ATTRIBUTE_ARCHIVE

SYMBOL_PLUS = "+"
SYMBOL_MINUS = "-"
# excel 每行的算式的数量
NUMBER_OF_EQUATIONS_PER_ROW = "number_of_equations_per_row"
# 生成的文件路径
EQUATION_FILE_PATH = "equation_file_path"
# 每次运行生成的xls张数
BATCH_COUNT = "batch_count"


_conf = {
    "simple_equation": {
        "up_bound": 20,
        "low_bound": 1,
        "generate_number": 100,
        "carry_or_abdication": True,
    },
    "combined_plus_equation": {
        "up_bound": 20,
        "low_bound": 1,
        "generate_number": 0,
        "carry_or_abdication": True,
    },
    "combined_minus_equation": {
        "up_bound": 20,
        "low_bound": 1,
        "generate_number": 0,
        "carry_or_abdication": True,
    },
    "mixed_equation": {
        "up_bound": 1,
        "low_bound": 1,
        "generate_number": 0,
        "carry_or_abdication": True,
    },
}


def load_conf(conf_path):
    config = configparser.ConfigParser()
    config.read(conf_path)

    sections = config.sections()
    for section in sections:
        for k in config[section]:
            _conf[k] = config[section][k]


def get_conf(name, default=""):
    if name in _conf:
        return _conf[name]
    else:
        return default
