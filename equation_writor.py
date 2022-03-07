import time
import uuid
import xlwt

from kousuan_conf import EQUATION_FILE_PATH, NUMBER_OF_EQUATIONS_PER_ROW, SYMBOL_MINUS, SYMBOL_PLUS, get_conf

EXCEL_CELL_SYMBOL_WIDTH = 1 * 256
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

    max_equation_length = 3
    for k in equations:
        if len(equations[k]) > max_equation_length:
            max_equation_length = len(equations[k])

    sheet_max_cells = get_conf(NUMBER_OF_EQUATIONS_PER_ROW, 5)*(max_equation_length+2)-1

    sheet.write_merge(0, 0, 0, sheet_max_cells, u"口算练习", style)
    sheet.write_merge(1, 1, 0, int(sheet_max_cells/2), u"用时:")
    sheet.write_merge(1, 1, int(sheet_max_cells/2) + 1, sheet_max_cells, u"得分:")

    i, j = 3, 0
    equation_count = 0
    sheet.row(i).height_mismatch = True
    sheet.row(i).height = EXCEL_CELL_HEIGHT
    for k in equations:
        for item in equations[k]:
            if item == SYMBOL_MINUS or item == SYMBOL_PLUS:
                sheet.col(j).width = EXCEL_CELL_SYMBOL_WIDTH
            else:
                sheet.col(j).width = EXCEL_CELL_WIDTH
            sheet.write(i, j, item, style)
            j += 1

        sheet.col(j).width = EXCEL_CELL_SYMBOL_WIDTH
        sheet.write(i, j, "=", style)
        sheet.col(j+1).width = EXCEL_CELL_WIDTH

        if len(equations[k]) < max_equation_length:
            j += max_equation_length - len(equations[k])

        j += 2

        equation_count += 1
        if equation_count == get_conf(NUMBER_OF_EQUATIONS_PER_ROW, 5):
            i += 1
            sheet.row(i).height_mismatch = True
            sheet.row(i).height = EXCEL_CELL_HEIGHT
            j = 0
            equation_count = 0

    uid = str(uuid.uuid4())[0:4]

    workbook.save("%s/ks_%s_%s.xls" % (get_conf(EQUATION_FILE_PATH),time.strftime("%m%d%H%M"),uid))
