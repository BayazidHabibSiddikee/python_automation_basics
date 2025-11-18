import openpyxl, csv, os
xl = os.makedirs('CSV-from-excel',exist_ok=True)
indir = '/home/curse/Documents'
for i in os.listdir(indir):
	if not i.endswith('.xlsx'):
		continue
	wb = openpyxl.load_workbook(os.path.join(indir,i))
	sheet = wb.active
	csv_filename = os.path.splitext(i)[0] + '.csv'
	a_file = open(os.path.join('CSV-from-excel',csv_filename),'w',newline='')
	b = csv.writer(a_file,delimiter='\t')
	for row in sheet.iter_rows(values_only=True):
		b.writerow(row)
		
