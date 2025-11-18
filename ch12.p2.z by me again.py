import openpyxl
wb = openpyxl.load_workbook('C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\automate resources\\produceSales.xlsx')
sheet = wb.active

update={'Garlic':3.07,'Celery':1.19,'Lemon':1.27}
for i in range(2,sheet.max_row+1):
    name = sheet['a'+str(i)].value #name= garlic
    if name in update:
        sheet['b'+str(i)]=update[name]
wb.save('ch12.p2.z updated.xlsx')

        
