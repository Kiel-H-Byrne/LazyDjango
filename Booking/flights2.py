import sys
import urllib2 as urllib
from urlparse import urlparse
import lxml
import pycurl
import cStringIO

from bs4 import BeautifulSoup as BS

from django.shortcuts import render_to_response
html_doc='none'

def get_price_html():
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
    title = ca_html.title.encode
    global days, dates, prices, title
    days = ca_html.select(".caldow")
    dates = ca_html.select(".caldate")
    prices = ca_html.select(".calprice")

#if __name__ == '__main__':
#    if len(sys.argv) != 2:
#        raise Exception("Incorrect number of arguments")
#    script, filename = sys.argv
#    if urlparse(filename).netloc:
#        f = urllib.urlopen(filename)
#    else:
#        f = open(filename, 'r')

def flights(request):
	get_price_html()
	get_ca_price()
	return render_to_response('flights.html',{'days':days, 'dates':dates, 'prices':prices, 'title':title})