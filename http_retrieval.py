# Pages extraction

import requests, bs4

import re

res = requests.get('https://www.infor.pl/akt-prawny/DZU.2018.174.0001735,ustawa-o-polskim-instytucie-ekonomicznym.html')

res.raise_for_status()

infor_soup = bs4.BeautifulSoup(res.content)

reg_expr = 'dziennik-ustaw/r2018/nr[1-9]+'

html = res.text

found = re.findall(reg_expr, html)

p_tags = infor_soup.select('p')

for x in p_tags[:]:
    print(x.get_text())