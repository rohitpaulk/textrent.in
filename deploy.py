print "Deployment Script in Python"

import os
username = os.environ['USERNAME']
print username
password = os.environ['PASS']
print password

host = 'textrent.in'

import ftplib

ftp = ftplib.FTP(host)
ftp.login(username,password)

data = []

ftp.dir(data.append)

ftp.quit()

for line in data:
    print "-", line



