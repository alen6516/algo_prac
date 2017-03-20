#####
# File Name: huffman.py
# Author: alen6516
# Created Time: 2017-03-12
#####

class Node:
    def __init__(self, freq):
        self.left=None
        self.right=None
        self.father=None
        self.freq=freq
    
    def get_right(self):
        return self.right

    def get_left(self):
        return self.left
        
    def get_father(self):
        return self.father
    
    def isLeft(self):
        return self.father.left == self     # this retuen a True/False

# build a Node
def createNodes(freqs):
    return [Node(freq) for freq in freqs]

# build a huffman tree    
def createHuffmanTree(nodes):
    # copy the input nodes to another list
    queue = nodes[:]

    while len(queue) > 1:   # while not converging into a root node
        # sorting by the freq attr of object item
        queue.sort(key=lambda item:item.freq)
        
        # define left, right, father node
        # pop out the first item of the list
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_right.freq + node_left.freq)
        
        # define the relation
        node_father.left = node_left
        node_father.right = node_right
        node_right.father = node_father
        node_left.father = node_father

        # add the father node at the last of the queue
        queue.append(node_father)
    
    queue[0].father = None
    return queue[0]

def huffmanEncoding(nodes, root):
    # declare that codes is a list of null char
    codes = [''] * len(nodes)
    for i in range (len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            
            node_tmp = node_tmp.father
    return codes

def regularize(string):
    chars = []i

    for i in string:
        freqs = string.count(string[i])

        for j in range(string):
            if string[j] == string[i]:
                del string[j]
        
        chars.append((string[i], freqs))

if __name__ == '__main__':
    #chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
    #freqs = [10,4,2,5,3,4,2,6,4,4,3,7,9,6]

    #chars_freqs = [('C', 2), ('G', 2), ('E', 3), ('K', 3), ('B', 4),
    #               ('F', 4), ('I', 4), ('J', 4), ('D', 5), ('H', 6),
    #               ('N', 6), ('L', 7), ('M', 9), ('A', 10)]

    string = raw_input('type something:')
    
    chars_freqs = regularize(string)





    nodes = createNodes([item[1] for item in chars_freqs])
    root = createHuffmanTree(nodes)
    codes = huffmanEncoding(nodes, root)
    for item in zip(chars_freqs, codes):
        print 'Character:%s    freq:%-2d    encoding: %s' % (item[0][0], item[0][1], item[1])
