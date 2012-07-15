import sys
import urllib2 as urllib
from urlparse import urlparse
import lxml
import pycurl
import cStringIO

from bs4 import BeautifulSoup as BS
from bs4 import Tag

from django.shortcuts import render_to_response
html_doc='none'

def get_html():
	zURL = 'https://caribbean.sita.aero/itd/itd/DoAirSearch'
	zARGS='_originSelected=Airport.JFK&'
	zARGS+='_destinationSelected=Airport.POS&'
	zARGS+='_tripType=Return&'
	zARGS+='_depdateeu=08/02/2013%20&'
	zARGS+='_retdateeu=18/02/2013%20&'
	zARGS+='_classType=Economy&_dateWindow=P3D&'
	zARGS+='_searchType=DatePriceLed&'
	zARGS+='requestor=AirSimpleReqsPage&'
	zARGS+='_channelLocale=en&'
	zARGS+='_children=0&'
	zARGS+='_adults=1&'
	zARGS+='_infants=0&'
	zARGS+='_seniors=0'
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
    global days, dates, prices, title, ca_html
    ca_html = BS(html_doc)
    title = ca_html.title
    days = ca_html.select(".headerrow")
    infos = ca_html.select(".datarow")
    Tag.do_not_call_in_templates = True

#if __name__ == '__main__':
# if len(sys.argv) != 2:
# raise Exception("Incorrect number of arguments")
# script, filename = sys.argv
# if urlparse(filename).netloc:
# f = urllib.urlopen(filename)
# else:
# f = open(filename, 'r')

def flights(request):
	get_html()
	get_ca_price()
	return render_to_response('flights.html',{'days':days,'infos':infos})