tbl_w = int(input('table width ='))
tbl_h = int(input('table height ='))
cell_w = int(input('cell_width ='))
cell_h = int(input('cell_height ='))

table_divide = tbl_w*('+' + '-'*cell_w) + '+\n'

table_box = cell_h*(('|' + ' ' * cell_w) * tbl_w + '|\n')

table_rows = tbl_h*(table_divide + table_box)

table = (table_rows + table_divide)

print(table)