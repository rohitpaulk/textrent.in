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

def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
upload(ftp, index.html)
ftp.quit()

for line in data:
    print "-", line



