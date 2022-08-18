import requests
from bs4 import BeautifulSoup
import re

sample_web_page = 'http://www.columbia.edu/~fdc/sample.html'
names = requests.get(sample_web_page)
head_line = BeautifulSoup(names.text, 'lxml')
print("Список заголовков h3 :")

# for heading in head_line.find_all(['h3']):
#     print( heading.text.strip())

text = names.text
result = re.findall(r'<h3 .*?>(.*?)</h3>', text)

if __name__ == "__main__":
    print(('\n'.join(result)))
