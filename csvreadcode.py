__author__ = 'Nispand'

import csv


def initlist():
    csvfile = open('all_month.csv','rb')
    csvreader = csv.reader(csvfile)
    csvreader.next()
    csvreader.next()
    count = 0
    latti = []
    longi = []
    for row in csvreader :
        print "lat ::" + row[1]
        print "long :: " + row[2]
    return "done"

initlist()