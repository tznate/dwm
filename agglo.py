# from scipy.cluster import hierarchy
# from scipy.spatial import distance
# import matplotlib.pyplot as plt

# points = [(0.40, 0.53), (0.22, 0.38), (0.35, 0.32), (0.26, 0.19), (0.08, 0.41), (0.45, 0.30)]
# names = ["p1", "p2", "p3", "p4", "p5", "p6"]

# x = distance.pdist(points, 'euclidean')

# # Plot the hierarchical clustering as a dendrogram.
# temp = hierarchy.linkage(x, 'ward')
# plt.figure()

# dn = hierarchy.dendrogram(temp, labels=names)

# plt.show()

import matplotlib.pyplot as plt
import csv
from scipy.cluster.hierarchy import dendrogram, linkage
with open('data_agglo.csv', 'r') as file:
    data = list(csv.reader(file))
    del data[0]
file.close()

linkage_data = linkage(data, metric='euclidean', method='complete')
print(linkage_data)
dendrogram(linkage_data, labels=[f'p{i+1}' for i in range(len(data))])
plt.title("Hierarchical Clustering : Aglomerative")
plt.show()
