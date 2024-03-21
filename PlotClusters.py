import matplotlib.pyplot as plt
def plotClusters(data,cls,out=None):
    if isinstance(data[0],int) or isinstance(data[0],float):
        for i in range(len(cls)):
            x = cls[i]
            plt.scatter(x,[0]*len(x),label=f"Cluster {i+1}")
        if out:
            x = out
            plt.scatter(x,[0]*len(x),label=f"Outliers",c='black')
    elif len(data[0])==2:
        for i in range(len(cls)):
            x, y = zip(*cls[i])
            plt.scatter(x,y,label=f"Cluster {i+1}")
        if out:
            x, y = zip(*out)
            plt.scatter(x,y,label=f"Outliers",c='black')
    elif len(data[0])==3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for i in range(len(cls)):
            x, y, z = zip(*cls[i])
            ax.scatter(x, y, z, marker='o',label=f"Cluster {i+1}")
        if out:
            x, y, z = zip(*out)
            ax.scatter(x, y, z, c='black', marker='o',label=f"Outliers")
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
    plt.legend()
    plt.show()