import requests
from bs4 import BeautifulSoup

"""results = soup.find(id='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')"""

page = requests.get('https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch')
soup = BeautifulSoup(page.content, 'html.parser')

page_title = soup.title.text
page_body = soup.body

print(page_title)
