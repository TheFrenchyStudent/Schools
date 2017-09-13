from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'http://www.enseignement-prive.info/etablissement/lycee-sainte-marie/ET059-620'

list_of_urls = ['http://www.enseignement-prive.info/etablissement/ecole-privee-primaire-notre-dame-du-tilleul/ET059-304'
,'http://www.enseignement-prive.info/etablissement/ecole-privee-saint-joseph/ET059-545'
,'http://www.enseignement-prive.info/etablissement/ecole-privee-maternelle-et-primaire-notre-dame-de-grace/ET059-302'
,'http://www.enseignement-prive.info/etablissement/ecole-privee-saint-joseph/ET059-371'
,'http://www.enseignement-prive.info/etablissement/elnon-nda-bcpst/ET059-639'
,'http://www.enseignement-prive.info/etablissement/ecole-privee-saint-jean-bosco-notre-dame-des-jeunes-groupe-marcq-institution/ET059-301'
,'http://www.enseignement-prive.info/etablissement/ecole-privee-jeanne-d-arc/ET059-347'
,'http://www.enseignement-prive.info/etablissement/institution-notre-dame-de-la-renaissance-ecole-notre-dame-de-la-renaissance/ET059-641'
,'http://www.enseignement-prive.info/etablissement/cpes-ipam-lille/ET059-598'
,'http://www.enseignement-prive.info/etablissement/ecole-privee-notre-dame-de-la-providence-institution-notre-dame-de-la-providence/ET059-366'
,'http://www.enseignement-prive.info/etablissement/ecole-privee-saint-adrien-la-salle/ET059-562'
,'http://www.enseignement-prive.info/etablissement/ecole-primaire-et-maternelle-privee-saint-jean/ET059-226'
,'http://www.enseignement-prive.info/etablissement/ensemble-scolaire-la-salle-lille-ecole-maternelle-et-primaire/ET059-314'
]

def fetch(url):
	print('\n\nCurrent : '+url)
	# Setting up the url requests thingy in a try/except to move on to the following URL in case of failure.
	try:
		temp = urlopen(Request(url, headers = {'User-agent' : 'Mozilla'}))
		url_opened = temp.read()
		temp.close()

		soup = BeautifulSoup(url_opened, 'html.parser')

	except:
		print('Could not process for :',url)
		return


		# Trying to find website adress and phone number. If one of them not found, keeps going.

	try:
		phone = soup.find('div', class_='icon-tel').span.a['href'][5:]
	except:
		phone = 'Not found'
		print('Phone not found for :\n',url)
		
	try:
		site = soup.find('div', class_='icon-site').a['href']
	except:
		site = 'Not found'
		print('Website adress not found for :\n', url)

	# Printing part, to be replace with Excel writing. Inch'Allah.
	print('Phone :', phone)
	print('Website adress :', site)
	
	

	

for url in list_of_urls:
	fetch(url)