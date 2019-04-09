rows=len(driver.find_element_by_xpath("html/body/table/tbody/tr"))
colums=len(driver.fine_element_by_xpath("html/body/table/tbody/tr/th[1]")
           print(rows)
           print(colums)

for r in range(1,rows+1)
    for c in range(1,colums+1)
    value= driver.find_element_by_xpath("html/body/table/tbody/").text()
    print(value)

import openpyxl

    path=""
    workbook=openc_load.workbook(path)
    sheet=workoboo.active()
    rows=sheet.max_rows()
    cols=sheet.max_closi)

for r in range(1,rows+1)
    for c in range(1,colums+1)
    print(sheet.cell(r=row, c=clols)).value()
    print(value)
