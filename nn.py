import matplotlib.pyplot as plt

def draw_model(layerList, save=False, show=False):

    plt.style.use('dark_background')
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


    for l in range(1,len(nodeList) ,1):

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
                #print(x,y)
                plt.plot(x, y, marker="o", color="darkslateblue")

    #print(matrix)
    plt.scatter([x], [y], marker='o', color="darkslateblue")

    plt.title('NerualNetworks')
    plt.xlabel('Layers')
    plt.ylabel('Nodes')

    plt.xticks([])
    plt.yticks([])

    if save:
        plt.savefig("nerualNetworks.png")

    if show:
        plt.show()


def layer_parser(summary):
    lines = summary.split("\n")
    
    layerList = []

    for line in lines:
        if "None" in line:
            data = list(set(line.split("  ")))
            for i in data:
                if "None" in i:
                    layerList.append([int(i.replace(" ", "").split(",")[0].replace("(", "")),None,int(i.replace(" ", "").split(",")[-1].replace(")", ""))])

    layerList.append([1])

    return layerList


def main():
    #tensorflow model.summary()
    summary = """
    Model: "sequential_1"
    _________________________________________________________________
    Layer (type)                Output Shape              Param #   
    =================================================================
    embedding_1 (Embedding)     (8, None, 8)              xxx     
                                                                    
    gru_1 (GRU)                 (4, None, 8)           xxx   
                                                                    
    dense_1 (Dense)             (4, None, 4)             xxx     
                                                                    
    =================================================================
    Total params: xxx (xx.xx MB)
    Trainable params: xxx (xx.xx MB)
    Non-trainable params: x (x.xx Byte)
    _________________________________________________________________
    """


    layerList = layer_parser(summary)
    # or
    # layer1 = [8, None, 8]
    # layer2 = [4,None,8]
    # layer3 = [4,None,4]
    # empty = [1] # don't delete
    # layerList = [layer1,layer2,layer3,empty]

    draw_model(layerList=layerList, show= True)

main()
