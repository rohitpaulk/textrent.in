print "Deployment Script in Python"

import os
password = os.environ['FTP_USERNAME']
print username
username = os.environ['FTP_PASS']
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



