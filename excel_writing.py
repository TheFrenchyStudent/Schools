import pandas
file = 'Pages inter écoles privées.xlsx'
xl = pandas.ExcelFile(file)
worksheet = xl.sheet_names[0]
#print(worksheet)

df = xl.parse(worksheet)
#col1 = df.iterrows()
#col = col1.set_index("New column_link")
df = df.set_index('New column_link')
test = df.iloc[1:10, 1:1]


#print(df.iloc[1:10, 1:1])

test_index = test.index

for x in test_index : 
	print(x)