import gspread

from parsing import getTable

gc = gspread.service_account(filename='nodal-condition-371319-1249feb577c3.json')
sh = gc.open_by_key("1wc4zgBNbgZIOt6y3WPtr5KYH6rw6ULF20z2ldSpH5Oo")
worksheet = sh.sheet1

table = getTable().split('\n')
row1 = [table[0], table[1]]
row2 = [table[2], table[3]]
row3 = [table[4], table[5]]
row4 = [table[6], table[7]]
row5 = [table[8], table[9]]
row6 = [table[10], table[11]]

worksheet.insert_row(row1, 1)
worksheet.insert_row(row2, 2)
worksheet.insert_row(row3, 3)
worksheet.insert_row(row4, 4)
worksheet.insert_row(row5, 5)
worksheet.insert_row(row6, 6)

