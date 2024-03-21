import numpy as np
import contextlib
import io
from PlotClusters import plotClusters
def DivCluster(nums):
    tp = False
    if isinstance(nums[0],tuple):
        tp = True
    n = len(nums)
    d = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if tp:
                if distmet == 'Euclidean':
                    d[i][j] = sum([(nums[i][k]-nums[j][k])**2 for k in range(len(nums[0]))])**0.5
                else:
                    d[i][j] = sum([abs(nums[i][k]-nums[j][k]) for k in range(len(nums[0]))])
            else:
                d[i][j] = abs(nums[i]-nums[j])
    a,b = nums.copy(),[]
    bi = []
    ai = list(range(len(a)))
    while len(a)>1:
        am = []
        sa = 0
        sb = 0
        for i in ai:
            for j in ai:
                sa += d[i][j]
            avga = sa/(len(ai)-1)
            for k in bi:
                sb += d[i][k]
            avgb = sb/len(bi) if len(bi)>0 else 0
            print(avga,"-",avgb)
            am.append(avga-avgb)
            sa=0
            sb=0
        print("am=",am)
        if len(bi)>0:
            cc=len(a)-1
            f=0
            for k,ad in zip(reversed(ai),reversed(am)):
                if ad>0:
                    print("cc=",cc)
                    print("a[cc]=",a[cc])
                    print("a before deleting a=",a)
                    b.append(a[cc])
                    del a[cc]
                    print("a after deleting a=",a)
                    ai.remove(k)
                    bi.append(k)
                    print("ai=",ai)
                    print("bi=",bi)
                    f=1
                cc-=1
            if f==0:
                break
        else:
            maxam = 0
            km = 0
            for k,ad in enumerate(am):
                if ad>maxam:
                    maxam = ad
                    km = k
            print("km=",km)
            b.append(a[km])
            del a[km]
            ai.remove(km)
            bi.append(km)
        print("a=",a)
        print("b=",b)
        print("ai=",ai)
        print("bi=",bi)
    return a,b
def computeDia(cls):
    c1 = list(set(cls))
    maxca = 0
    tp = False
    if isinstance(cls[0],tuple):
        tp = True
    for i in range(len(c1)):
        for j in range(i+1,len(c1)):
            if tp:
                if distmet == 'Euclidean':
                    dt = sum([(cls[i][k]-cls[j][k])**2 for k in range(len(cls[0]))])**0.5
                else:
                    dt = sum([abs(cls[i][k]-cls[j][k]) for k in range(len(cls[0]))])
            else:
                dt = abs(c1[i]-c1[j])
            if dt>maxca:
                maxca=dt
    return maxca
def printClusters(cls):
    for i in range(len(cls)):
        print(f"Cluster {i+1} = {cls[i]}")
    print()
K = 3
data = [(1,2),(3,4),(2.5,4),(1.5,2.5),(3,5),(2.8,4.5),(2.5,4.5),(1.2,2.5),(1,3),(1,5),(1,2.5),(5,6),(4,3)]
#data = [13.5,4.5,16,12,9.5,7,6,6,8.5,12,14.5,11,2.5,6,16,13,16,5.5,6.5,9,8.5,14.5,5.5,4.5,8.5]
#data = [(5,4,7),(7,3,1),(6,4,9),(5,5,2),(9,10,4),(12,4,6),(7,11,7),(6,1,0)]
data = list(set(data))
#distmet = 'Manhattan'
distmet = 'Euclidean'
with contextlib.redirect_stdout(io.StringIO()):
    A,B = DivCluster(data)
print("First 2 CLusters :")
cl = [A,B]
printClusters(cl)
rnd = lambda x:round(x,2 if isinstance(data[0],tuple) else 0)
if K>2:
    while len(cl)!=len(data):
        maxdia = -1
        for i,c in enumerate(cl,start=1):
            if len(c)<2:
                continue
            maxd = computeDia(c)
            if maxd>maxdia:
                maxdia = maxd
                clid = i-1
            print(f"Dia of Cluster {i} = {rnd(maxd)}")
        print(f"Max Dia = {rnd(maxdia)} of Cluster {clid+1} : {cl[clid]}")
        print()
        with contextlib.redirect_stdout(io.StringIO()):
            C1,C2 = DivCluster(cl[clid])
        print("New CLusters =",C1,C2)
        print()
        cl.remove(cl[clid])
        cl.extend([C1,C2])
        printClusters(cl)
        if len(cl)==K:
            break
plotClusters(data,cl)