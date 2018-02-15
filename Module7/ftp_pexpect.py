#!/usr/bin/env python

import pexpect
import sys
import getpass

#username and host are provided through the cli as an argument after the call of the program
#they are delimited with a @ e.g. user@ftp_host
if '@' in sys.argv[1]:
    user = sys.argv[1].split('@')[0]
    host = sys.argv[1].split('@')[1]
else:
    sys.exit(1)

passwd = getpass.getpass('Provide a password:')

id = pexpect.spawn('ftp %s'%host)

id.expect_exact('Name')
id.sendline(user)
id.expect_exact('Password')
id.sendline(passwd)
id.expect_exact('ftp')

print id.before
print id.after

id.sendline('dir')

id.expect_exact('ftp')
lines =  id.before.split('\n')

for line in lines:
    print line 

