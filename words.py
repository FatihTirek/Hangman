from requests import get
from bs4 import BeautifulSoup

source = get('http://www.uefap.com/vocab/select/awl.htm').text
soup = BeautifulSoup(source, 'html.parser')
word_list = soup.find_all('tr')

del word_list[0]
