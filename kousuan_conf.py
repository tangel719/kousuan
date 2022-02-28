

import configparser
from stat import FILE_ATTRIBUTE_ARCHIVE

SYMBOL_PLUS = "+"
SYMBOL_MINUS = "-"
# excel 每行的算式的数量
NUMBER_OF_EQUATIONS_PER_ROW = "number_of_equations_per_row"
# 生成算式的总数
NUMBER_OF_EQUATIONS = "number_of_equations"
# 算式中的最大数字，及n以内的算式
UPPER_BOUND_OF_NUMBER = "upper_bound_of_number"
# 连加题的数量
NUMBER_OF_COMBINED_PLUS_EQUATIONS = "number_of_combined_plus_equations"
# 连减题的数量
NUMBER_OF_COMBINED_MINUS_EQUATIONS = "number_of_combined_minus_equations"
# 混合运算题的数量
NUMBER_OF_MIXED_EQUATIONS = "number_of_mixed_equations"
# 生成的文件路径
EQUATION_FILE_PATH = "equation_file_path"



_conf = {
    NUMBER_OF_EQUATIONS_PER_ROW: 5,
    NUMBER_OF_EQUATIONS: 100,
    UPPER_BOUND_OF_NUMBER: 20,
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
