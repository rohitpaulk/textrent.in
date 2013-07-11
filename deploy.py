print "Deployment Script in Python"

import os
password = os.environ['FTP_PASS']+'!'
username = os.environ['FTP_USERNAME']
host = 'textrent.in'

import ftplib

ftp = ftplib.FTP_TLS(host)
ftp.login(username,password)
ftp.prot_p()

data = []

ftp.dir(data.append)

ftp.quit()

for line in data:
    print "-", line



