#!/usr/bin/env python

import sys
from optparse import OptionParser
import mechanize


def validate_proxy(proxy_url):
    
    if proxy_url.startswith('https') or proxy_url.startswith('http'):
        #strip the http:// or the https:// prefixes
        proxy_url = proxy_url.lstrip('https://')
    
    #Check that the proxy has the form url:port with length 2
    if len(proxy_url.split(":")) == 2:
        return True
    else:
        return False

def main():
   
    parser = OptionParser(usage="usage: %prog url [options]")

    parser.add_option('-p','--proxy',dest='proxy', help='Proxy server')


    (options, args) = parser.parse_args()

    if len(args) !=1:
        parser.error("Incorrect number of arguments provided!")
        #parser.print_help()
        sys.exit(1)

    url = args[0]
    proxy = options.proxy

    if not proxy:
        parser.error("No proxy provided")
        sys.exit(1)
        
    
    br = mechanize.Browser()
    br.set_handle_robots(False)
    print "\nUsing proxy: %s" %proxy

    if validate_proxy(proxy):
        br.set_proxies({"http": proxy})
    else:
        print("No valid proxy url form provided (e.g. proxy:port or localhost:8080 )")
        sys.exit(1)    


    print "Now Openining URL: %s" % url
    br.open(url)
    
    print "Printing all the links found in the provided page"
    print "================================================="

    for link in br.links():
         print link.text+": " + link.url


if __name__ == "__main__":
    main()
