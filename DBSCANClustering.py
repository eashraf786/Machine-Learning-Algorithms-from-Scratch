import matplotlib.pyplot as plt
import pandas as pd
from PlotClusters import plotClusters
import pyperclip
"""
Mode 1 = 1-D Data
Mode 2 = 2-D Data
Mode 3 = 3-D Data
Mode 4 = From clipboard
"""
mode = 2
if mode==1:
    data = [13.5,4.5,16,12,9.5,7,6,6,8.5,12,14.5,11,2.5,6,16,13,16,5.5,6.5,9,8.5,14.5,5.5,4.5,8.5]
elif mode==2:
    data = [(1,2),(3,4),(2.5,4),(1.5,2.5),(3,5),(2.8,4.5),(2.5,4.5),(1.2,2.5),(1,3),(1,5),(1,2.5),(5,6),(4,3)]
elif mode==3:
    data = [(1,2,1.4),(3,4,1.7),(2.5,4,4.1),(1.5,2.5,6.2),(3,5,3.5),(2.8,4.5,1.1),(2.5,4.5,4.1),(1.2,2.5,3.7),(1,3,7),(1,5,4),(1,2.5,0.8),(5,6,1.2),(4,3,3.4)]
elif mode==4:
    data = pyperclip.paste().split()
    data = [float(d) for d in data]
minpts = 2
eps = 0.5
distmet = 'euclidean'
#distmet = 'manhattan'
if isinstance(data[0],tuple):    
    if distmet == 'euclidean':
        dist = lambda x,y: sum([(x[k]-y[k])**2 for k in range(len(x))])**0.5
    else:
        dist = lambda x,y: sum([abs(x[k]-y[k]) for k in range(len(x))])
else:
    dist = lambda x,y: abs(x-y)
data2 = data.copy()
def findneighbors(p,clu):
    nb = []
    for d in reversed(data2):
        if d not in clu and d!=p:
            dt = dist(p,d)
            if dt<=eps:
                nb.append(d)
    return nb
cls = []
out = []
for d in data2[:]:
    if d not in data2:
        continue
    cl = []
    #print("Finding neighbors of ",d)
    cl = findneighbors(d,cl)+[d]
    #print(cl)
    if len(cl)==1 and d not in out:
        out.append(d)
        data2.remove(d)
    if len(cl)>=minpts:
        #print("deleted",d)
        data2.remove(d)
        #print("deleting ",cl)
        data2 = list(set(data2) - set(cl))
        #print("data2 after deleting =",data2)
        for c in cl:
            nb = findneighbors(c,cl)
            #print(f"{len(nb)} new neighbor {nb} found core p = {c}")
            data2 = list(set(data2) - set(nb))
            cl.extend(nb)
        #print(cl)
        cls.append(cl)
    #print("data2 =",data2)
out += data2
for i,c in enumerate(cls):
    print(f"Cluster {i+1} = {cls[i]}")
print("Outliers")
print(out)
plotClusters(data,cls,out)