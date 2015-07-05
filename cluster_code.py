__author__ = 'Nispand'

import csv
import numpy as np
import matplotlib.pyplot as plt
from csvreadcode import initlist
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

list1 = []
list2 = []
list1,list2 = initlist()
xcord = []
ycord = []
csvfile = open('nispand.csv','rb')
csvreader = csv.reader(csvfile)
csvreader.next()
csvreader.next()
i = 0
j= 0
for row in csvreader :
        xcord.append(list1.index(row[6]))
        ycord.append(list2.index(row[7]))

tot = []
for x in range(0,xcord.__len__()):
        a = []
        xp = xcord[x]
        yp = ycord[x]
        a = [xp,yp]
        tot.append(a)

X = np.array(tot)
print type(X)
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

colors = ["g.","r."]

for i in range(len(X)):
        print("coordinate:",X[i],"label:",labels[i])
        plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize = 10)

plt.scatter(centroids[: , 0],centroids[: , 1],marker= "x",s =100,linewidths=3,zorder = 10)
plt.show()