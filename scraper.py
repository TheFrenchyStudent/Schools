from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'http://www.enseignement-prive.info/etablissement/lycee-sainte-marie/ET059-620'

def fetch(url):
	###print('\n\nCurrent : '+url)
	# Setting up the url requests thingy in a try/except to move on to the following URL in case of failure.
	try:
		temp = urlopen(Request(url, headers = {'User-agent' : 'Mozilla'}))
		url_opened = temp.read()
		temp.close()

		soup = BeautifulSoup(url_opened, 'html.parser')

	except:
		###print('Could not process for :',url)
		return


	# Trying to find website adress and phone number. If one of them not found, keeps going.

	try:
		phone = soup.find('div', class_='icon-tel').span.a['href'][5:]
	except:
		phone = 'Not found'
		###print('Phone not found for :\n',url)
		
	try:
		site = soup.find('div', class_='icon-site').a['href']
	except:
		site = 'Not found'
		###print('Website adress not found for :\n', url)

	
	return [url, site, phone]
