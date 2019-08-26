import sys
import os
import re
import collections
from bs4 import BeautifulSoup
from stemming.porter2 import stem

listOfFiles = os.listdir(sys.argv[1])
path = 'C:\Users\harri\PycharmProjects\IR_assignment1\corpus\\'
openStopList = open("C:\Users\harri\PycharmProjects\IR_assignment1\stoplist.txt", 'r')
stopwords = openStopList.read()
stopList = stopwords.split("\n")

terms = {}
termid = 1

documents = collections.defaultdict(list)

for x in range(len(listOfFiles)):
    openFile = open(path + listOfFiles[x], 'r')
    data = openFile.read()
    index = data.find("<!DOCTYPE")
    data = data[index:]
    soup = BeautifulSoup(data, 'html.parser')
    parseSoup = soup.get_text()
    p = re.split("\\W+(\\.?\\W+)*", parseSoup)
    p = filter(None, p)
    p = [z.lower() for z in p]
    for y in range(len(p)):
        if p[y] not in stopList:
            p[y] = stem(p[y])
            if p[y] not in terms:
                terms[p[y]] = termid
                documents[(str(x), termid)].append(y)
                termid += 1
            else:
                documents[(str(x), terms[p[y]])].append(y)

f = open('docids.txt', 'w')
for x in range(len(listOfFiles)):
    f.write(str(x) + "\t" + listOfFiles[x] + "\n")
f.close()

with open('termids.txt', 'w') as f:
    for key, value in terms.items():
        f.write('%s\t%s\n' % (value, key))

with open('doc_index.txt', 'w') as f:
    for key, value in documents.items():
        f.write('%s\t%s\t' % (key[0], key[1]))
        for x in range(len(value)):
            f.write('%s\t' % value[x])
        f.write('\n')