from requests import get
import bs4

source = get('http://www.uefap.com/vocab/select/awl.htm').text

soup = bs4.BeautifulSoup(source, 'html.parser')

word_list = soup.find_all('tr')

del word_list[0]