#!/usr/bin/env python

import math
from operator import itemgetter
from Tools import *

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
  	documentList = file2dict('a2.docs')
  	queryList = file2dict('a2.qrys')
	avgLen = avgDocLength(documentList)
	print "Diagnostics"
	print "Total no. of documents: " + str(len(documentList))
	print "Avg document length: " + str(avgLen)
	for queryKey in queryList:
		for documentKey in documentList:
#			print "Doc: " + str(documentList[documentKey]) + " Query: " + str(queryList[queryKey])
			result = weightedsum(documentList[documentKey], queryList[queryKey], documentList, avgLen)
			if result > 0:
				output += str(queryKey) + " 0 " + str(documentKey) + " 0 " + str(result) + " 0\n"
	writeFile(output,'tfidf.top')
	print "Done. File: tfidf.top"
