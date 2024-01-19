import matplotlib.pyplot as plt

plt.style.use('dark_background')


emb = [64/32, None, 256/32]
gru = [128/32, None, 256/32]
dense = [128/32, None, 65/32]

emty = [1] # don't delete

layerList = [emb, gru, dense, emty]

layers = []

for i in range(len(layerList)):
    for j in range(len(layerList[i])):
        if j == 1:
            continue
        layers.append(layerList[i][j])

layers = dict(enumerate(layers))

maximum = 0
x = []
y = []

for a in range(len(layers)):
    if layers[a] > maximum:
        maximum = layers[a]

maximum = int(maximum)

for a in range(len(layers)):
    x += [a for i in range(0, maximum, int(maximum/layers[a]))]
    y += [i  for i in range(0, maximum, int(maximum/layers[a]))]


matrix = [x, y]
rows, cols = len(matrix), len(matrix[0])

transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        transposed_matrix[j][i] = matrix[i][j]

matrix = transposed_matrix

maxy = 0
for i in matrix:
    if i[0] > maxy:
        maxy = i[0]


nodeList = []

for i in range(maxy):
    row = []
    for j in matrix:
        if i == j[0]:
            row.append(j)
    nodeList.append(row)


for l in range(len(nodeList)):

    list1 = nodeList[l-1]
    list2 = nodeList[l]

    edges = []
    for i in list1:
        row = []
        for j in list2:
            row.append([i, j])
        edges.append(row)



    for i in edges:
        for j in i:
            x = [j[0][0], j[1][0]]
            y = [j[0][1], j[1][1]]
            print(x,y)
            plt.plot(x, y, marker="o", color="darkslateblue")

print(matrix)




plt.scatter([x], [y], marker='o', color="darkslateblue")

plt.title('NerualNetworks')
plt.xlabel('Layers')
plt.ylabel('Nodes')

plt.xticks([])
plt.yticks([])

#plt.savefig("nerualNetworks.png")

plt.show()
