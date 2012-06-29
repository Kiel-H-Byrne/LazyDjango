import sys
import urllib2 as urllib
from urlparse import urlparse
import lxml

from bs4 import BeautifulSoup as BS

def get_ca_price(html_doc):
    ca_html = BS(html_doc)
    print ca_html.title
    prices = ca_html.select(".calprice")
    for price in prices:
        print "Your ticket will be %s" % price.text
        print ""
    print "woot"


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("Incorrect number of arguments")
    script, filename = sys.argv
    if urlparse(filename).netloc:
        f = urllib.urlopen(filename)
    else:
        f = open(filename, 'r')
    get_ca_price(f)
