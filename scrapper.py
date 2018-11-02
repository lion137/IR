# Scrapping part


import requests, bs4, re, webbrowser
from functools import reduce
from operator import add


def retrieve_year_urls(year):
    """Returns all the links to Monitor Polski
    from a given year (web: infor.pl)"""
    html = 'http://www.infor.pl/dziennik-ustaw/r' + str(year) + '/'
    res = requests.get(html)
    res.raise_for_status()
    reg_expr = 'dziennik-ustaw/r' + str(year) + '/nr[0-9]+'
    html_main = res.text
    found_links_main = re.findall(reg_expr, html_main)
    str_prep = "http://www.infor.pl"
    return list(map(lambda x: str_prep + "/" + x, found_links_main))



def extract_child_links(link):
    """Returns links to documents on
    subsides of given Monitor Polski year"""
    links_set = set()
    str_prep = "http://www.infor.pl"
    res = requests.get(link)
    res.raise_for_status()
    html_link = res.text
    html = html_link.split()
    pattern = re.compile('/akt-prawny/DZU')
    pattern1 = re.compile("\.html")
    for token in html:
        search = pattern.search(token)
        if search:
            links_set.add(str_prep + token[search.span()[0] : pattern1.search(token).span()[1]])
    return list(links_set)


def retrieve_text(link):
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.content)
    p_tags = soup.select('p')
    pattern = re.compile('(class=\"p\d)|(class=\"MsoNormal)|(class=\"dt[nzu])')
    tags = []
    for x in p_tags:
        if pattern.search(str(x)):
            tags.append(x)
    def g_text(x):
        return x.get_text()
    return reduce(add, [x.split() for x in map(g_text, tags)])


if __name__ == '__main__':
    a_list = [retrieve_year_urls(x) for x in range(2014, 2018)]
    a_child_links = [extract_child_links(x) for x in a_list[1][:5]]
    a_text = [retrieve_text(x) for x in a_child_links]
    print(a_text[:10])
