import time

import xlwt

from kousuan_conf import NUMBER_OF_EQUATIONS_PER_ROW, get_conf

EXCEL_CELL_WIDTH = 3 * 256
EXCEL_CELL_HEIGHT = 2 * 256


def write_to_file(equations):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Sheet1")

    style = xlwt.XFStyle()
    alignment = xlwt.Alignment()
    # 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
    alignment.horz = 0x02
    # 0x00(上端对齐)、 0x01(垂直方向上居中对齐)、0x02(底端对齐)
    alignment.vert = 0x01
    style.alignment = alignment

    sheet.write_merge(0, 0, 0, get_conf(NUMBER_OF_EQUATIONS_PER_ROW, 5)*5-1, u"口算练习", style)
    sheet.write_merge(1, 1, 0, get_conf(NUMBER_OF_EQUATIONS_PER_ROW, 5)*5-1,
                      u"用时:                             得分:                    ")

    i, j = 3, 0
    equation_count = 0
    sheet.row(i).height_mismatch = True
    sheet.row(i).height = EXCEL_CELL_HEIGHT
    for k in equations:
        print(equations[k])
        for item in equations[k]:
            sheet.col(j).width = EXCEL_CELL_WIDTH
            sheet.write(i, j, item, style)
            j += 1

        sheet.col(j).width = EXCEL_CELL_WIDTH
        sheet.write(i, j, "=", style)
        sheet.col(j+1).width = EXCEL_CELL_WIDTH
        j += 2

        equation_count += 1
        if equation_count == get_conf(NUMBER_OF_EQUATIONS_PER_ROW, 5):
            i += 1
            sheet.row(i).height_mismatch = True
            sheet.row(i).height = EXCEL_CELL_HEIGHT
            j = 0
            equation_count = 0

    workbook.save("/Users/tangyigang/Desktop/ks_" +
                  time.strftime("%m%d%H%M")+'.xls')
