from ftplib import FTP, error_perm
import os

def ftpDownloader(stationId, startYear, endYear, host='ftp.pyclass.com', user='student@pyclass.com', password='student123'):
    ftp = FTP(host)
    ftp.login(user, password)
    print(ftp.nlst())

    if not os.path.exists('C:\\in'):
        os.mkdir('C:\\in')
    os.chdir('C:\\in')

    for year in range(startYear, endYear+1):
        fullpath = '/Data/%s/%s-%s.gz' %(year, stationId, year)
        filename = os.path.basename(fullpath)
        try:

            with open(filename, 'wb') as file:
                ftp.retrbinary('RETR %s' %fullpath, file.write)
                print('%s file is downloaded' %filename)



        except error_perm:
            print('%s is not available' %filename)

            os.remove(filename)

ftpDownloader('010010-99999', 1982, 1986)