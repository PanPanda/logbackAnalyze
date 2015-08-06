import ftplib
import os
import socket
import sys
import time
from datetime import date

HOST = 	''
USER_NAME = 'logback'
PASS_WORD = 'logback'
FILE = 'cap.log'
DIR = ''
FILE_NAME = ''

def DownLoadFile(date):
	try:
		f = ftplib.FTP(HOST)
	except(socket.error, socket.gaierror) as e:
		print('ERROR:cannot connect %s' % HOST)
		return 
	print('******Connected to %s' % HOST)


	try:
		f.login(USER_NAME,PASS_WORD)
	except ftplib.error_perm:
		print('ERROR:cannot login USER_NAME=%s,PASS_WORD=%s' % (USER_NAME,PASS_WORD))
		f.quit()
		return
	print('***Logined in as %s' % USER_NAME)

	try:
		dir = '/' + date + DIR
		f.cwd(dir)
		#f.dir()
	except ftplib.error_perm:
		print('ERROR:cannot cd to %s' % dir)

	try:
		file_name = 'cap.' + date + '.log'
		file = open(file_name,'wb')
		f.retrbinary('RETR %s' %file_name, file.write)
		file.close()
	except ftplib.error_perm:
		print('ERROR:cannot read file %s' % file_name)
		os.unlink(file_name)
		file.close()
	else:
		print('***DownLoad %s to %s' % (file_name,os.getcwd()))
	f.quit()
	return

if __name__ == '__main__':
	DownLoadFile(sys.argv[1])
	today = date.today()
	today.isoformat()
	print(today)
