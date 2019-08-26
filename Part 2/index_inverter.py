import collections

inverted_index = collections.defaultdict(list)

lines = open('C:\Python27\doc_index.txt').read().splitlines()
for x in range(len(lines)):
    lines[x] = lines[x].split('\t')

for x in range(len(lines)):
    for y in range(len(lines[x])-1):
        if y > 1:
            inverted_index[lines[x][1]].append((lines[x][0], lines[x][y]))

listOfTerms = inverted_index.keys()

for x in range(len(listOfTerms)):
    inverted_index[listOfTerms[x]].sort(key=lambda tup: (int(tup[0]), int(tup[1])))

with open('term_index.txt', 'w') as f:
    for key, value in inverted_index.items():
        f.write('%s\t' % key)
        for x in range(len(value)):
            if x == 0:
                f.write('%s:%s\t' % (value[x][0], value[x][1]))
                temp = int(value[x][0])
                temp2 = int(value[x][1])
            else:
                if int(value[x][0]) == temp:
                    f.write('%s:%s\t' % (str(int(value[x][0])-temp), str(int(value[x][1])-temp2)))
                    temp = int(value[x][0])
                    temp2 = int(value[x][1])
                else:
                    f.write('%s:%s\t' % (str(int(value[x][0]) - temp), value[x][1]))
                    temp = int(value[x][0])
                    temp2 = int(value[x][1])
        f.write('\n')

offsets = [0]
f = open('C:\Python27\\term_index.txt', 'r')
for line in iter(f.readline, ''):
    offsets.append(f.tell())
f.close()

openFile = open('term_info.txt', 'w')
with open('C:\Python27\\term_index.txt', 'r') as f:
    for offset in offsets:
        f.seek(offset)
        currentLine = f.readline().split('\t')
        numOfDocs = 0
        for x in range(len(currentLine)-1):
            if x > 0:
                if currentLine[x].split(':')[0] != '0':
                    numOfDocs += 1
        openFile.write('%s\t%s\t%s\t%s\n' % (currentLine[0], offset, str(len(currentLine)-2), str(numOfDocs)))
openFile.close()
