#!/usr/bin/env python
import urllib



#create a url with special characters 
url = "http://www.test.com/special=$@#!%*()}"

#encode_url = urllib.urlencode(url)
#print encode_url

encode_quote = urllib.quote(url.encode('utf8'))
print encode_quote

encode_quote_plus = urllib.quote_plus(url.encode('utf8'))
print encode_quote_plus

