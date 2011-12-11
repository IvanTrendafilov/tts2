#from numpy import *
import os
from operator import itemgetter

def file2dict(filename):
	_file = readFile(filename)
	_file = _file.split('\n')
	file_dict = dict()
	for line in _file:
		line_split = line.split(None)
		if(line_split != []):
			value = line_split[1:]
			value = [x for x in value if x]		
			file_dict[line_split[:1][0]] = value
	return file_dict

def readFile(filename):
	f = open(filename, 'r')
	try:
	    content = f.read()
	finally:
	    f.close()
	return content
	
def writeFile(data, filename):
	d = dict()
	string = ''
	array = []
	s = set(array)	
	f = open(filename, 'w')
	try:
	    if type(data) == type(string):
	    	f.write(data)
	    if type(data) == type(array):
	    	for d in data:
			f.write(str(d) + '\n')
	    if type(data) == type(s):
		data = list(data)	    	
		for d in data:
			f.write(str(d) + '\n')
	    if type(data) == type(d):
		sortedData = sorted(data.items(), key=itemgetter(0))
		for sd in sortedData:
			f.write(str(sd) + '\n')
	finally:
	    f.close()
	



