# scraping data

from imports import *
from temp_data import ht

def retrieve_years_urls():
    """retrieves year urls"""
    html_prep = "http://prawo.sejm.gov.pl/isap.nsf/ByYear.xsp?type=WDU&" + "year="
    return [html_prep + str(x) for x in list(range(1918, 1940)) + list(range(1944, 2019))]

def retrieve_year_volumes(year):
    """retrieves volume url's of a given year """
    html_prep = "http://prawo.sejm.gov.pl/isap.nsf/ByYear.xsp?type=WDU&year=" + str(year)
    resp = requests.get(html_prep)
    resp.raise_for_status()
    html_main = resp.text
    pattern = re.compile("vol=[\d]+")
    length = len(re.findall(pattern, html_main))
    links = [html_prep + "&vol=" + str(x) for x in range(1, length + 1)]
    return links


if __name__ == '__main__':
    print(retrieve_year_volumes(2011))
