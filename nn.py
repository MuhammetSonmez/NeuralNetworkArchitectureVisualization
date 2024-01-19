import matplotlib.pyplot as plt

plt.style.use('dark_background')


emb = [64/32, None, 256/32]
gru = [128/32, None, 256/32]
dense = [128/32, None, 65/32]

layerList = [emb, gru, dense]

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

embNodes1 = []
embNodes2 = []
gruNodes1 = []
gruNodes2 = []
denseNodes1 = []
denseNodes2 = []

matrix = [x, y]
rows, cols = len(matrix), len(matrix[0])

transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        transposed_matrix[j][i] = matrix[i][j]

matrix = transposed_matrix

embNodes1 = []
embNodes2 = []
gruNodes1 = []
gruNodes2 = []
denseNodes1 = []
denseNodes2 = []

for i in matrix:
    if i[0] == 0:
        embNodes1.append(i)
    elif i[0] == 1:
        embNodes2.append(i)
    elif i[0] == 2:
        gruNodes1.append(i)
    elif i[0] == 3:
        gruNodes2.append(i)
    elif i[0] == 4:
        denseNodes1.append(i)
    elif i[0] == 5:
        denseNodes2.append(i)

for i in embNodes1:
    for j in embNodes2:
        x_emb = [i[0], j[0]]
        y_emb = [i[1], j[1]]

        plt.plot(x_emb, y_emb, marker="o", color="darkslateblue")

for i in embNodes2:
    for j in gruNodes1:
        x_embGru = [i[0], j[0]]
        y_embGru = [i[1], j[1]]

        plt.plot(x_embGru, y_embGru, marker="o", color="darkslateblue")

for i in gruNodes1:
    for j in gruNodes2:
        x_gru = [i[0], j[0]]
        y_gru = [i[1], j[1]]

        plt.plot(x_gru, y_gru, marker="o", color="darkslateblue")

for i in gruNodes2:
    for j in denseNodes1:
        x_gruDense = [i[0], j[0]]
        y_gruDense = [i[1], j[1]]
        plt.plot(x_gruDense, y_gruDense, marker="o", color="darkslateblue")

for i in denseNodes1:
    for j in denseNodes2:
        x_dense = [i[0], j[0]]
        y_dense = [i[1], j[1]]

        plt.plot(x_dense, y_dense, marker="o", color="darkslateblue")

plt.scatter([x], [y], marker='o', color="darkslateblue")

plt.title('NerualNetworks')
plt.xlabel('Layers')
plt.ylabel('Nodes')

plt.xticks([])
plt.yticks([])

plt.savefig("nerualNetworks.png")

#plt.show()
