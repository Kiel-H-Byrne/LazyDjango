import sys
import urllib2 as urllib
from urlparse import urlparse
import lxml
import pycurl
import cStringIO

from bs4 import BeautifulSoup as BS

html_doc=0
def get_html():
	zURL = 'https://caribbean.sita.aero/itd/itd/DoAirSearch'
	zARGS='_originSelected=Airport.JFK&_destinationSelected=Airport.POS&_tripType=Return&_depdateeu=08/02/2013%20&_retdateeu=18/02/2013%20&_classType=Economy&_dateWindow=P3D&_searchType=DatePriceLed&requestor=AirSimpleReqsPage&_channelLocale=en&_children=0&_adults=1&_infants=0&_seniors=0'

	buf = cStringIO.StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, zURL)
	c.setopt(c.POSTFIELDS, zARGS)
	c.setopt(c.WRITEFUNCTION, buf.write)	
	c.perform()
	global html_doc
	html_doc=buf.getvalue()
	buf.close()

def get_ca_price():
    ca_html = BS(html_doc)
    print ca_html.title
    days = ca_html.select(".caldow")
    dates = ca_html.select(".caldate")
    prices = ca_html.select(".calprice")
    
    for day in days:
        print "%s" % day
    
    for date in dates:
        print "%s" % date.text
    
    for price in prices:
        print "Your ticket will be %s" % price.text
    print "<a href='#'>Home</a>"

#if __name__ == '__main__':
#    if len(sys.argv) != 2:
#        raise Exception("Incorrect number of arguments")
#    script, filename = sys.argv
#    if urlparse(filename).netloc:
#        f = urllib.urlopen(filename)
#    else:
#        f = open(filename, 'r')
	
get_html()
get_ca_price()