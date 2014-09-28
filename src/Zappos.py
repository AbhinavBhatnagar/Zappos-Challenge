import urllib2
import json
import sys

response = urllib2.urlopen('http://api.zappos.com/Search?term=nike&key=52ddafbe3ee659bad97fcce7c53592916a6bfd73&limit=20')
#pyresponse = (json.dumps(json.load(response), indent=4, sort_keys=True))
pyresponse = json.load(response)   
print json.dumps(pyresponse)
#print pyresponse.keys()

		





