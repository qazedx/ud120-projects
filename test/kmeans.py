from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

x = [1,2,6,5,4,8,5,8,90,70,80,30]
y = [5,6,4,8,5,2,8,6,70,50,60,90]
z = [[1,2],[6,5],[4,8],[50,80],[90,70],[80,30]]
clf  = KMeans(n_clusters=3)
k=0
g=[]
for a in y:
   g.append([a,x[k]])
   k=k+1

clf.fit(g)
# pred = clf
pred = clf.predict(g)
print pred
print g
colors = ["g", "b","r"]
# plt.scatter(x,y,color=colors[pred])
for i  ,k in enumerate(g):
    # print pred[h]
    plt.scatter(g[i][0],g[i][1], color = colors[pred[i]])
    print i
    # print j
# print g[j]
# for i in z:
#     plt.scatter(z[0],z[1],color="r")
plt.show()