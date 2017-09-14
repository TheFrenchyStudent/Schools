import scraper, excel_writing, excel_reading
import pandas
# Set object
source_urls = excel_reading.read_excel('Pages inter écoles privées.xlsx','New column_link')
#source_urls = ['http://www.enseignement-prive.info/etablissement/ecole-privee-sainte-anne/ET059-524'
#,'http://www.enseignement-prive.info/etablissement/ecole-privee-cardinal-lienart/ET059-527'
#,'http://www.enseignement-prive.info/etablissement/ecole-privee-sainte-marie/ET059-529'
#,'http://www.enseignement-prive.info/etablissement/ecole-privee-du-sacre-coeur/ET059-53'
#,'http://www.enseignement-prive.info/etablissement/ecole-privee-saint-joseph/ET059-530'
#,'http://www.enseignement-prive.info/etablissement/ecole-privee-saint-augustin/ET059-532'
#]


df = pandas.DataFrame(columns=['Source URL','Website','Phone'])

index = 0
for url in source_urls:
	entry = scraper.fetch(url)
	df.loc[index] = entry
	index += 1
		
excel_writing.excel_writer(df)