from Tools import *
query_file = readFile('a2.qrys')
doc_file = readFile('a2.docs')
doc_file = doc_file.split('\n')
query_file = query_file.split('\n')
doc_dict = dict()
query_dict = dict()
print "Working..."
for line in doc_file:
	line_split = line.split(None)
	tmp = set(line_split[1:]) # create a set from the tags
	tmp = [x for x in tmp if x] # remove '' tags
	if line_split != []:
		doc_dict[line_split[:1][0]] = tmp # insert them in the dictionary

for line in query_file:
	line_split = line.split(None)
	tmp = set(line_split[1:])
	tmp = [x for x in tmp if x] # remove '' 
	if line_split != []:
		query_dict[line_split[:1][0]] = tmp

while '' in doc_dict:
	del doc_dict['']
while '' in query_dict: 
	del query_dict['']

output = ""
for key in query_dict.keys():
	for key2 in doc_dict.keys():
		inters = [val for val in query_dict[key] if val in doc_dict[key2]]
		if len(inters) > 0:
			output = output + str(key) + " 0 " + str(key2) + " 0 " + str(len(inters)) + " 0\n"

writeFile(output, 'overlap.top')


