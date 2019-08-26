import sys
from stemming.porter2 import stem

if sys.argv[1] == '--doc':

    print 'Listing for document:\t',
    print sys.argv[2]

    lines = open('C:\Python27\docids.txt', 'r').read().splitlines()
    for x in range(len(lines)):
        lines[x] = lines[x].split('\t')
        if lines[x][1] == sys.argv[2]:
            docID = lines[x][0]
            break

    print 'DOCID:\t',
    print docID

    distinctTerms = 0
    totalTerms = 0

    docDetails = open('C:\Python27\doc_index.txt', 'r').read().splitlines()
    for x in range(len(docDetails)):
        docDetails[x] = docDetails[x].split('\t')
        if docDetails[x][0] == docID:
            distinctTerms += 1
            totalTerms += len(docDetails[x]) - 3

    print 'Distinct terms:\t',
    print distinctTerms

    print 'Total terms:\t',
    print totalTerms

elif sys.argv[1] == '--term':

    if len(sys.argv) == 3:
        print 'Listing for term:\t',
        print sys.argv[2]

        term = sys.argv[2]
        term = stem(term)

        lines = open('C:\Python27\\termids.txt', 'r').read().splitlines()
        for x in range(len(lines)):
            lines[x] = lines[x].split('\t')
            if lines[x][1] == term:
                termID = lines[x][0]
                break

        print 'TERMID:\t',
        print termID

        termsInfo = open('C:\Python27\\term_info.txt', 'r').read().splitlines()
        for x in range(len(termsInfo)):
            termsInfo[x] = termsInfo[x].split('\t')
            if termsInfo[x][0] == termID:
                print 'Number of documents containing term:\t',
                print termsInfo[x][3]
                print 'Term frequency in corpus:\t',
                print termsInfo[x][2]
                print 'Inverted list offset:\t',
                print termsInfo[x][1]
                break

    else:
        print 'Inverted list for term:\t',
        print sys.argv[2]
        print 'In document:\t',
        print sys.argv[4]

        term = sys.argv[2]
        term = stem(term)

        lines = open('C:\Python27\\termids.txt', 'r').read().splitlines()
        for x in range(len(lines)):
            lines[x] = lines[x].split('\t')
            if lines[x][1] == term:
                termID = lines[x][0]
                break

        print 'TERMID:\t',
        print termID

        lines2 = open('C:\Python27\docids.txt', 'r').read().splitlines()
        for x in range(len(lines2)):
            lines2[x] = lines2[x].split('\t')
            if lines2[x][1] == sys.argv[4]:
                docID = lines2[x][0]
                break

        print 'DOCID:\t',
        print docID

        termsInfo = open('C:\Python27\\term_info.txt', 'r').read().splitlines()
        for x in range(len(termsInfo)):
            termsInfo[x] = termsInfo[x].split('\t')
            if termsInfo[x][0] == termID:
                byteOffset = termsInfo[x][1]
                print 'Inverted list offset:\t',
                print byteOffset
                break

        term_index = open('C:\Python27\\term_index.txt', 'r')
        term_index.seek(int(byteOffset))
        details = term_index.readline()
        term_index.close()
        termFreq = 0
        flag = 0
        positions = []
        details = details.split('\t')
        for x in range(len(details)-1):
            if x > 0:
                if x == 1:
                    if details[x].split(':')[0] == docID:
                        termFreq += 1
                        flag = 1
                        positions.append(int(details[x].split(':')[1]))
                        basePosition = int(details[x].split(':')[1])
                        continue
                    else:
                        base = int(details[x].split(':')[0])
                        continue
                if flag == 1:
                    if details[x].split(':')[0] == '0':
                        termFreq += 1
                        basePosition += int(details[x].split(':')[1])
                        positions.append(basePosition)
                        continue
                    else:
                        break
                base += int(details[x].split(':')[0])
                if base == int(docID):
                    termFreq += 1
                    flag = 1
                    positions.append(int(details[x].split(':')[1]))
                    basePosition = int(details[x].split(':')[1])

        print 'Term frequency in document:\t',
        print termFreq
        print 'Positions:\t',
        print positions
else:
    print "Invalid command..."
