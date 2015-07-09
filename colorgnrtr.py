__author__ = 'Nispand'


import colorsys

def get_N_HexCol(N=5):

    HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in xrange(N)]
    hex_out = []
    for rgb in HSV_tuples:
        rgb = map(lambda x: int(x*255),colorsys.hsv_to_rgb(*rgb))
        hex_out.append(rgb)
    return hex_out

new = list(set(labels))
count =0
for lab in new :
    print ("Number of points in each Cluster ",lab)
    for items in labels:
        if (items == lab):
            count +=1
    print (count)
    count = 0
centroid = km.cluster_centers_
print (centroid)
print (" Distance Between Clusters ")
for i in range (len(km.cluster_centers_)):
    x1 = centroid[i][0]
    y1 = centroid[i][1]
    x=i
    for j in range(x+1,len(km.cluster_centers_)):
        x2 = centroid[j][0]
        y2 = centroid[j][1]
        distance = np.sqrt((y2-y1)**2 + (x2-x1)**2)
        print (distance)

