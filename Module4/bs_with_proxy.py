#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup
from optparse import OptionParser

#function to validate the proxy
def validate_proxy(proxy_url):
    
    if proxy_url.startswith('https') or proxy_url.startswith('http'):
        #strip the http:// or the https:// prefixes
        proxy_url = proxy_url.lstrip('https://')
    
    #Check that the proxy has the form url:port with length 2
    if len(proxy_url.split(":")) == 2:
        return True
    else:
        return False


#main
def main():
   
    #parser for the arguments and options
    parser = OptionParser(usage="usage: %prog url [options]")
    parser.add_option('-p','--proxy',dest='proxy', help='Proxy server')


    (options, args) = parser.parse_args()

    if len(args) !=1:
        parser.error("Incorrect number of arguments provided!")
        #parser.print_help()
        sys.exit(1)

    site = args[0]
    proxy = options.proxy

    if not proxy:
        parser.error("No proxy provided")
        sys.exit(1)

    #validate the proxy provided by the user
    if validate_proxy(proxy):
        proxy = urllib2.ProxyHandler({'http':proxy})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
    else:
        print("No valid proxy url form provided (e.g. proxy:port or localhost:8080 )")
        sys.exit(1)  

    #open the url provided and save the result in the response object
    response = urllib2.urlopen(site)
    #read the response object for the page contents
    html = response.read()

    #parse the html site with the BeatifulSoup lxml parser
    bs = BeautifulSoup(html, 'lxml')

    #search for the page links
    a_href = bs.find_all('a')

    for link in a_href:
        if link['href']:
            print link.text + ': ' + link['href']


if __name__ == "__main__":
    main()
