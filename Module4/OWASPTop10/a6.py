#!/usr/bin/env python
'''
'''

import mechanize

url = 'http://192.168.1.10/mutillidae/'

dirs = ['documentation', 'images']



def dirlist():
    browser = mechanize.Browser()

    for directory in dirs:
    
        request_url = url + directory

        print '[!] Currently Testing {0} \n'.format(request_url)
        response = browser.open(request_url)

        page = response.read()

        if 'Index of' in page:
            print '[+] The web server allows directory listing!'
            break




def getforPOST():
    browser = mechanize.Browser()

    url = 'http://192.168.1.10/mutillidae/index.php?page=user-info.php&username=jeremy&password=password&user-info-php-submit-button=View+Account+Details'

    response = browser.open(url)

    page = response.read()

    if 'Results' in page:
        print '[+] The server supports GET for POST and hence is vulnerable'



def main():
    dirlist()
    getforPOST()

if __name__=='__main__':
    main()
