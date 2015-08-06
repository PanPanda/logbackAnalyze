import ftplib
import os
import socket
import sys
import time
from datetime import date

HOST = 	''
USER_NAME = ''
PASS_WORD = ''
FILE = 'cap.log'

def DownLoadFile(file_name):
	try:
		f = ftplib.FTP(HOST)
	except(socket.error, socket.gaierror) as e:
		print('ERROR:cannot connect %s' % HOST)
		return 
	print('******Connected to %s' % HOST)

if __name__ == '__main__':
	DownLoadFile(sys.argv[1])
	today = date.today()
	today.isoformat()
	print(today)
