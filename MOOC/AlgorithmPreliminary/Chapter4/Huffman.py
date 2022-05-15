import math

class Node(object):
    def __init__(self, name=None, value=None):
        self._name = name
        self._value = value
        self._left = None
        self._right = None
        
class HuffmanTree(object):
    def __init__(self, char_weights):
        self.Leav = [Node(part[0], part[1]) for part in char_weights]
        while len(self.Leav) != 1:
            self.Leav.sort(key=lambda node:node._value, reverse=True)
            c = Node(value=(self.Leav[-1]._value + self.Leav[-2]._value))
            c._left = self.Leav.pop(-1)
            c._right = self.Leav.pop(-1)
            self.Leav.append(c)
        self.root = self.Leav[0]
        self.Buffer = list(range(10))

    def pre(self, tree, length):
        node = tree
        if not node:
            return
        elif node._name:
            print(f"{node._name} encoding:", end='')
            for i in range(length):
                print(self.Buffer[i], end='')
            print('')
            return
        self.Buffer[length] = 0
        self.pre(node._left, length + 1)
        self.Buffer[length] = 1
        self.pre(node._right, length + 1)
    
    def get_code(self):
        self.pre(self.root, 0)

if __name__ == '__main__':
    S = [('A', 25), ('B', 13), ('C', 12), ('D', 9), ('E', 8), ('F', 6), ('G', 3), ('n/', 1)]
    result = HuffmanTree(S)
    print(result.get_code())
