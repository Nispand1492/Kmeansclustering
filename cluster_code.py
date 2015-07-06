__author__ = 'Nispand'

import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from csvreadcode import initlist
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
nof = raw_input("Enter number of clusters::")
#list1 = []
#list2 = []
#list1,list2 = initlist()
xcord = []
ycord = []
csvfile = open('all_month.csv','rb')
csvreader = csv.reader(csvfile)
csvreader.next()
csvreader.next()
i = 0
j= 0
for row in csvreader :
        print "latt :: " + row[1]
        xcord.append(row[1])
        print "long :: " + row[2]
        ycord.append(row[2])

tot = []
for x in range(0,xcord.__len__()):
        a = []
        xp = xcord[x]
        yp = ycord[x]
        a = [xp,yp]
        tot.append(a)

X = np.array(tot)
print type(X)
kmeans = KMeans(n_clusters=int(nof))
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

colors = ["g.","r.",".c"]

for i in range(len(X)):
        print("coordinate:",X[i],"label:",labels[i])
        plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize = 10)

plt.scatter(centroids[: , 0],centroids[: , 1],marker= "x",s =100,linewidths=3,zorder = 10)
plt.show()