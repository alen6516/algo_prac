class Node:
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq
        
    def isLeft(self):
        return self.father.left == self

def createNodes(freqs):
    return [Node(freq) for freq in freqs]

def createHuffmanTree(nodes):
    queue = nodes[:]
    while len(queue)>1 :
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)    
        node_right = queue.pop(0)    
        node_father = Node(node_left.freq + node_right.freq)

        # relation
        node_father.left = node_left
        node_father.right = node_right

        node_left.father = node_father
        node_right.father = node_father

        queue.append(node_father)
    
    queue[0].father = None
    return queue[0]

def huffmanEncoding(nodes, root):
    codes = ['']*len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes

if __name__ == '__main__':
    temp = raw_input(">> input: ")
    string = list(temp)
    char = []
    ch_fr = []
    for i in range(len(string)):
        if string[i] not in char:
            ch_fr.append((string[i],string.count(string[i])))
            char.append(string[i])
        else:
            pass

    ch_fr.sort(key = lambda item: item[1])
    
    print(ch_fr)
    '''
    input will look like:
    chars_freqs = [('C', 2), ('G', 2), ('E', 3), ('K', 3), ('B', 4),
                   ('F', 7), ('I', 4), ('J', 4), ('D', 5), ('H', 6),
                   ('N', 6), ('L', 7), ('M', 9), ('A', 10)]
    '''
    nodes = createNodes([item[1] for item in ch_fr])
    root = createHuffmanTree(nodes)

    codes = huffmanEncoding(nodes, root)
    for item in zip(ch_fr, codes):
        print("character:%s  freq:%-2d   encoding %s" % (item[0][0], item[0][1], item[1]))
