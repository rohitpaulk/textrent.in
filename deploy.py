print "Deployment Script in Python"

import os
password = os.environ['FTP_USERNAME']
print password
username = os.environ['FTP_PASS']
print username

host = 'textrent.in'

import ftplib

ftp = ftplib.FTP(host)
ftp.login(username,password)

data = []

ftp.dir(data.append)

ftp.quit()

for line in data:
    print "-", line



