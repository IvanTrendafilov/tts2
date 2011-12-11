# IvanRank-13
# Tf.Idf with Sound Ex spelling correction
# and Hack-Translation
# NOTE: You need to change the line
# queryList = file2dict('a2.qrys')
# to run with test.qrys


import math
import re
from operator import itemgetter
from Tools import *

def hackTranslate(word):
	wordMap = {'water':['voda','vittel','vatten','vann','ilma','vatn','vanduo'],'tree':['pyebwa','pohon','strom','mti','stablo','coed','copac','trees'],'sky':['lucht','nebu','qiell','cielo','dangus','himmel','ceo','skies','sy','sk','ky'],'people':['mennesker','ljudje','ljudi','pessoas','emberek','persoas','les-gens','person','peple','peopl'],'grass':['nyasi','trawy','iarba','hierba','trava','rumput'],'buildings':['foirgnimh','mga-gusali','bangunan','gebouwen','edifici','budynki','pastatai','edificios','building'],'plane':['ndege','odrzutowych','jet','pesawat','avionom','airplane','eroplano','het-vliegtuig','letadlo','vliegtuig'],'mountain':['montagna','mal','hory','gunung','de-montagne','planine','hegy','sliabh'],'deer':['ree'],'flowers':['flower','fjuri','blomster','lule','flori','blommor','les-fleurs','kwiaty','flors'],'clouds':['chmury','oblaki','mraky','debesys','ulap','nuvens','nuvole','cloud'],'snow':['neve','sniegs','neu','sneeu','sneachta','sne','sneeuw','la-neige'],'birds':['adar','ptica','fuglar','les-oiseaux','vogels','bird','fugle'],'stone':['stones','piatra','akmens','klip','sten','cloch','batu'],'grass':['gras'],'field':['fields','lapangan','cerrig','veld','polja','gelanggang','campos'],'bear':['bears','orso','ariu','medve','polaire','oso','medvjed','polare','polarni'],'street':['streets','ulica','triq','kalye','ulice','strada','straat'],'garden':['kert','zahrada','gardens','giardino']}
	for key in wordMap:
		if word in wordMap[key]:
			return key
	return word

def soundEx(word):
	firstLetter = word[0:1].upper()
	rest = word[1:len(word)].lower()
	rest = re.sub('[r]', '6', rest)
	rest = re.sub('[mn]', '5', rest)
	rest = re.sub('[l]','4', rest)
	rest = re.sub('[dt]','3', rest)
	rest = re.sub('[cgjkqsxz]','2', rest)
	rest = re.sub('[bfpv]','1',rest)
	rest = re.sub('[hw]', '', rest)
	rest = re.sub('1[1]+','1',rest)
	rest = re.sub('2[2]+','2',rest)
	rest = re.sub('3[3]+','3',rest)
	rest = re.sub('4[4]+','4',rest)
	rest = re.sub('5[5]+','5',rest)
 	rest = re.sub('6[6]+','6',rest)
	rest = re.sub('[a-z]+','',rest)
	
	while len(rest) < 3:
		rest += '0'
	rest = rest[0:3]
	return firstLetter + rest

def List2SoundEx(wordList):
	codeList = []
    	for word in wordList:
        	codeList.append(soundEx(hackTranslate(word)))
    	return codeList
  
def file2dictS(filename):
	_file = readFile(filename)
	_file = _file.split('\n')
	file_dict = dict()
	for line in _file:
		line_split = line.split(None)
		if(line_split != []):
			value = line_split[1:]
			value = [x for x in value if x]		
			file_dict[line_split[:1][0]] = List2SoundEx(value)
	return file_dict

def avgDocLength(documentList):
	totalDocLength = 0
	for document in documentList:
		totalDocLength += len(documentList[document])
	return totalDocLength / float(len(documentList))

def wordCount(document):
  	return len(document)

def numDocsContaining(word,documentList):
	count = 0
	for document in documentList:
		if word in documentList[document]:
			count += 1
  	return count

def tf(word, document):
	return document.count(word)

def idf(word, documentList):
	return math.log10(len(documentList) / float(numDocsContaining(word,documentList))) if numDocsContaining(word,documentList) else 0

def weightedsum(document, query, documentList, avgLen):
	w_sum = 0
	for word in query:
		if tf(word, document) != 0: # optimisation, as if tf = 0, then the sum = 0
			w_sum += (tf(word, query) * tf(word, document)) / (tf(word, document) + ( 2 * len(document)/float(avgLen))) * idf(word, documentList)
	return w_sum
	


if __name__ == '__main__':
	result = dict()
	output = ""
	print "Processing"
  	documentList = file2dictS('a2.docs')
  	queryList = file2dictS('a2.qrys')
	avgLen = avgDocLength(documentList)
	print "Diagnostics"
	print "Total no. of documents: " + str(len(documentList))
	print "Avg document length: " + str(avgLen)
	print "Working..."
	for queryKey in queryList:
		for documentKey in documentList:
#			print "Doc: " + str(documentList[documentKey]) + " Query: " + str(queryList[queryKey])
			result = weightedsum(documentList[documentKey], queryList[queryKey], documentList, avgLen)
			if result > 0:
				output += str(queryKey) + " 0 " + str(documentKey) + " 0 " + str(result) + " 0\n"
	writeFile(output,'best.top')
	print "Done. File: best.top"
