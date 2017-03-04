#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup
from optparse import OptionParser

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

    site = args[0]
    proxy = options.proxy

    if not proxy:
        parser.error("No proxy provided")
        sys.exit(1)

    if validate_proxy(proxy):
        proxy = urllib2.ProxyHandler({'http':proxy})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
    else:
        print("No valid proxy url form provided (e.g. proxy:port or localhost:8080 )")
        sys.exit(1)  


    response = urllib2.urlopen(site)
    html = response.read()

    bs = BeautifulSoup(html, 'lxml')

    a_href = bs.find_all('a')

    for link in a_href:
        if link['href']:
            print link.text + ': ' + link['href']


if __name__ == "__main__":
    main()
