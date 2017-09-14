import xlsxwriter
import pandas

def excel_writer(dataframe):
	
	
	writer = pandas.ExcelWriter('DB écoles.xlsx', engine = 'xlsxwriter')
	dataframe.to_excel(writer, sheet_name = 'Ecoles privées')
	writer.save() 


	