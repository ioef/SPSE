#!/usr/bin/env python
'''
'''

import mechanize

url = 'http://192.168.1.10/mutillidae/'

dirs = ['documentation', 'images']



browser = mechanize.Browser()

for directory in dirs:
    
    request_url = url + directory

    print '[!] Currently Testing {0} \n'.format(request_url)
    response = browser.open(request_url)

    page = response.read()

    if 'Index of' in page:
        print '[+] The web server allows directory listing!'
        break





