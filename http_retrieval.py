# Pages extraction

import requests , bs4
import re
import sqlite3

main_html = 'http://www.infor.pl/dziennik-ustaw/r2017/'
some_law_html = 'http://www.infor.pl/akt-prawny/DZU.2018.174.0001735,ustawa-o-polskim-instytucie-ekonomicznym.html'



#daughter_side_html = 'http://www.infor.pl/dziennik-ustaw/r2018/nr180/'
daughter_side_html = 'https://www.infor.pl/dziennik-ustaw/r2017/nr252/'

# Main side:
res = requests.get(main_html)
res.raise_for_status()

# First subside:
res_daughter_side = requests.get(daughter_side_html)
res_daughter_side.raise_for_status()

# Regexes:
reg_expr_main_side = 'dziennik-ustaw/r2017/nr[0-9]+'
regex_daughter_side = '/akt-prawny/DZU'

# Soup object and links, main
main_side_soup = bs4.BeautifulSoup(res.content)
html_main = res.text
found_links_main = re.findall(reg_expr_main_side, html_main)
main_side_p_tags = main_side_soup.select('p')
'''for x in main_side_p_tags:
    print(x.get_text())'''

#Soup object and links daughter
daughter_soup = bs4.BeautifulSoup(res_daughter_side.content)
html_daughter  = res_daughter_side.text
found_daughter_links = re.findall(regex_daughter_side, html_daughter)
daughter_side_p_tags = daughter_soup.select('p')

# Print found links on daughter side:
#print(found_daughter_links, len(found_daughter_links))
#print(html_daughter.split())

def extract_links_main(html_string, reg_pattern, str_prep):
    found_links = re.findall(reg_pattern, html_string)
    return list(map(lambda x: str_prep + "/" + x, found_links))


def extract_links_daughter(html_string, reg_pattern, str_prep):
    links_set = set()
    html = html_string.split()
    pattern = re.compile(reg_pattern)
    pattern1 = re.compile("\.html")
    for token in html:
        search = pattern.search(token)
        if search:
            links_set.add(str_prep + token[search.span()[0] : pattern1.search(token).span()[1]])
    return list(links_set)

#links = extract_links_daughter(html_daughter, regex_daughter_side, "http://www.infor.pl")

#links1 = extract_links_main(html_main, reg_expr_main_side, 'http://www.infor.pl')
#import webbrowser
#print(links)


#print(found_links_main, len(found_links_main))




