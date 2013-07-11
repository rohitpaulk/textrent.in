print "Deployment Script in Python"

import os
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
host = 'textrent.in'

import ftplib

ftp = ftplib.FTP(host)
ftp.login(username,password)

data = []

ftp.dir(data.append)

ftp.quit()

for line in data:
    print "-", line



