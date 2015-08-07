#-*- encoding: utf-8 -*-
import re
import sys
import os

def isFileExists(strFile):
	return os.path.isfile(strFile)

def SearchKeyWord(keyWord, fileName):
	if(isFileExists(fileName) == False):
		print ('file %s not exists' % fileName)
		sys.exit()

	print '************************'
	print '%s' % fileName
	print '************************'

	linenum = 1
	findlinenum = 0
	findtime = 0

	file_object = open('data.txt', 'w')
	
	
	with open(fileName,'r') as fread:
		lines = fread.readlines()
		for line in lines:
			rs = re.search(keyWord, line)
			if rs:
				sys.stdout.write('line: %d' %linenum)
				file_object.write(line)
				lsstr = line.split(keyWord)
				strlength = len(lsstr)
				findtime = findtime + (strlength - 1)
				findlinenum = findlinenum + 1
			linenum = linenum + 1

		print('******************')
		print ('find keyWord times %d' %findlinenum)
	file_object.close()

if __name__ == '__main__':
	SearchKeyWord('手机充值','cap.2015-08-01.log')
	
