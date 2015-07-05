__author__ = 'Nispand'

import csv


def initlist():
    csvfile = open('nispand.csv','rb')
    csvreader = csv.reader(csvfile)
    csvreader.next()
    csvreader.next()
    count = 0
    procat = []
    prosubcat = []
    for row in csvreader :
        if row[6] not in procat:
            procat.append(row[6])
        if row[7] not in prosubcat:
            prosubcat.append(row[7])
    return procat,prosubcat

