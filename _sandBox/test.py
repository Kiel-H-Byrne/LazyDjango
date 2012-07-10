import urllib
import urllib2

xml='_originSelected=Airport.JFK&_destinationSelected=Airport.POS&_tripType=Return&_depdateeu=08/02/2013%20&_retdateeu=18/02/2013%20&_classType=Economy&_dateWindow=P3D&_searchType=DatePriceLed&requestor=AirSimpleReqsPage&_channelLocale=en&_children=0&_adults=1&_infants=0&_seniors=0'
request_data = urllib.urlencode({"DATA": xml})
response = urllib2.urlopen("https://caribbean.sita.aero/itd/itd/DoAirSearch", request_data)

response_data = response.read()
data = response_data.split('\n')
print data