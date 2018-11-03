# scraping data

from imports import *

from temp_data import *


def retrieve_years_urls():
    """retrieves year urls"""
    html_prep = "http://prawo.sejm.gov.pl/isap.nsf/ByYear.xsp?type=WDU&" + "year="
    return [html_prep + str(x) for x in list(range(1918, 1940)) + list(range(1944, 2019))]


def retrieve_year_volumes_to_2011(year):
    """retrieves volume url's of a given year """
    html_prep = "http://prawo.sejm.gov.pl/isap.nsf/ByYear.xsp?type=WDU&year=" + str(year)
    resp = requests.get(html_prep)
    resp.raise_for_status()
    html_main = resp.text
    pattern = re.compile("vol=[\d]+")
    length = len(re.findall(pattern, html_main))
    links = [html_prep + "&vol=" + str(x) for x in range(1, length + 1)]
    return links

def retrieve_page_with_download(link):
    """retrieves page with download links"""
    html_prep = 'http://prawo.sejm.gov.pl/isap.nsf/'
    resp = requests.get(link)
    resp.raise_for_status()
    html_main = resp.text
    pattern = re.compile("DocDetails.xsp\?id=WDU[0-9]+")
    return [html_prep + x for x in re.findall(pattern, html_main)]


def retrieve_download_link(link):
    """:returns pdf download link"""
    html_prep = "http://prawo.sejm.gov.pl"
    resp = requests.get(link)
    resp.raise_for_status()
    html_m = resp.text
    pattern = re.compile(r"/isap.nsf/download.xsp[A-Za-z0-9/]+\.pdf")
    if not "uznany za uchylony" in ht:
        link = re.findall(pattern, html_m)
        try:
            link = link[0]
            return html_prep + re.findall(pattern, html_m)[0]
        except Exception:
            print("retrieve_download_link: no valid link on site")


if __name__ == '__main__':
    lin = retrieve_year_volumes_to_2011(2010)[0]
    link = retrieve_page_with_download(lin)
    #print(lin)
    #print(link)
    print(retrieve_download_link(link[0]))