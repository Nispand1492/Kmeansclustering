__author__ = 'Nispand'
"""

Name :: Nispand Mehta

Section :: 3.30 -5.30 pm

UTA ID :: 1001163146
Links Referred::
https://www.youtube.com/watch?v=ZS-IM9C3eFg
https://forums.freebsd.org/threads/numpy-cannot-import-scimath.45468/
http://stackoverflow.com/questions/18176591/importerror-no-module-named-matplotlib-pyplot
http://stackoverflow.com/questions/1273203/cant-import-numpy-in-python
http://stackoverflow.com/questions/25815567/problems-with-numpy-in-pycharm
https://www.google.com/search?q=get+index+of+an+element+in+list&ie=utf-8&oe=utf-8#q=find+index+of+element+in+list+python
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans


def clusterplot():
        nof = raw_input("Enter number of clusters::")
        xcord = []
        ycord = []
        csvfile = open('all_month.csv','rb')
        csvreader = csv.reader(csvfile)
        csvreader.next()
        csvreader.next()
        i = 0
        j = 0

        for row in csvreader :
                xcord.append(row[1])
                ycord.append(row[2])

        tot = []
        for x in range(0,xcord.__len__()):
                a = []
                xp = xcord[x]
                yp = ycord[x]
                a = [xp,yp]
                tot.append(a)

        X = np.array(tot)
        #print type(X)
        kmeans = KMeans(n_clusters=int(nof))
        kmeans.fit(X)
        centroids = kmeans.cluster_centers_
        labels = kmeans.labels_
        cnt = {}
        #print(centroids)
        #print(labels)
        colors = ["g.","r.","c.","b.","m.","y.","k.","w."]
        inicnt = 0
        for i in range(len(X)):
                #print("coordinate:",X[i],"label:",labels[i])
                clr = str(colors[labels[i]])
                plt.plot(X[i][0],X[i][1],clr,markersize = 10)
                if clr not in cnt:
                        cnt[clr] = 0
                else :
                        cnt[clr] = cnt[clr] + 1

        for i in range(len(centroids)):
                x1 = centroids[i][0]
                y1 = centroids[i][1]
                x = i
                for j in range(x+1,len(centroids)):
                        x2 = centroids[j][0]
                        y2 = centroids[j][1]
                        distance = np.sqrt((y2-y1)**2 + (x2-x1)**2)
                        print "Distance between  points:: [ " + str(x1) + "," + str(y1) + "] and ["+str(x2) + ","+str(y2) + "]::"
                        print(distance)

        for key in cnt :
                inicnt = inicnt + 1
                print "Number of points in Cluster ::" + str(inicnt) +":: "+ str(cnt[key])

        plt.scatter(centroids[: , 0],centroids[: , 1],marker= "x",s =100,linewidths=3,zorder = 10)
        plt.show()
        return tot

def getcoordi(x_param,y_param):
        xcord = []
        ycord = []
        csvfile = open('all_month.csv','rb')
        csvreader = csv.reader(csvfile)
        csvreader.next()
        csvreader.next()
        i = 0
        j = 0

        for row in csvreader :
                xcord.append(row[1])
                ycord.append(row[2])

        tot = []
        for x in range(0,xcord.__len__()):
                a = []
                xp = xcord[x]
                yp = ycord[x]
                a = [xp,yp]
                tot.append(a)
        return tot

def for_bargraph(x_param,y_param,nof):
        xcord = []
        ycord = []
        csvfile = open('all_month.csv','rb')
        csvreader = csv.reader(csvfile)
        csvreader.next()
        csvreader.next()
        i = 0
        j = 0

        for row in csvreader :
                xcord.append(row[1])
                ycord.append(row[2])

        tot = []
        for x in range(0,xcord.__len__()):
                a = []
                xp = xcord[x]
                yp = ycord[x]
                a = [xp,yp]
                tot.append(a)

        X = np.array(tot)
        #print type(X)
        kmeans = KMeans(n_clusters=int(nof))
        kmeans.fit(X)
        centroids = kmeans.cluster_centers_
        labels = kmeans.labels_
        cnt = {}
        data = {}
        #print(centroids)
        #print(labels)
        colors = ["g.","r.","c.","b.","m.","y.","k.","w."]
        inicnt = 0
        for i in range(len(X)):
                #print("coordinate:",X[i],"label:",labels[i])
                clr = str(colors[labels[i]])
                plt.plot(X[i][0],X[i][1],clr,markersize = 10)
                if clr not in cnt:
                        cnt[clr] = 0
                else :
                        cnt[clr] = cnt[clr] + 1
        keycnt = 1
        for key in cnt:
                data[i] = cnt[key]
                keycnt = keycnt + 1

        return cnt