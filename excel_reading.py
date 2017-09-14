import pandas


def read_excel(filename, column_name):
	# Transforms a column from an excel file into a python set, to be used in other modules.
	file, col = str(filename), str(column_name)
	result = set()


	xl = pandas.ExcelFile(file)
	worksheet = xl.sheet_names[0]
	# xl.parse turns a worksheet into a pandas DataFrame
	df = xl.parse(worksheet)

	for index, row in df.iterrows():
		result.add(row[col])

	return result

#read_excel('Pages inter écoles privées.xlsx','New column_link')

