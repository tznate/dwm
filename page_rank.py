#Page Rank#

import networkx as nx
import pylab as plt
D = nx.DiGraph()
n = int(input('Enter number of nodes:'))
for i in range(n):
    print(f"\nEnter node {i}:")
    D.add_weighted_edges_from(
        [(input("Enter Parent:"), input("Enter Child:"), int(input("Enter Weight:")))])
print("\nPageRank:", nx.pagerank(D))
nx.draw(D, with_labels=True)
plt.show()

#  Output
# Enter number of nodes:4

# Enter node 0:
# Enter Parent:A
# Enter Child:B
# Enter Weight:1

# Enter node 1:
# Enter Parent:A
# Enter Child:C
# Enter Weight:1

# Enter node 2:
# Enter Parent:C
# Enter Child:A
# Enter Weight:1

# Enter node 3:
# Enter Parent:B
# Enter Child:C
# Enter Weight:1

# PageRank: {'A': 0.387789442707259, 'B': 0.21481051315058508, 'C': 0.3974000441421556}
