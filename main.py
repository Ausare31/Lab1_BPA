import requests
from bs4 import BeautifulSoup
url = 'https://omgtu.ru/ecab/persons/index.php?b=1'
page = requests.get(url)
page_parsed = BeautifulSoup(page.text, 'html.parser')
employees = page_parsed.findAll('div', style="padding: 5px; font-size: 120%;")
with open('result.txt', 'w') as f:
    for employee in employees:
        name = employee.find('a').text.strip()
        f.write(name + '\n')
