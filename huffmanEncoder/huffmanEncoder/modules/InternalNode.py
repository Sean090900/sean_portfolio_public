# Creator: Sean Dickson

class InternalNode():

    def __init__(self, charSum, freqSum, left, right):
        """
        This class is used to build leaf nodes for a Huffman Encoding Tree
        """
        self.character = charSum
        self.frequency = freqSum
        self.left = left
        self.right = right 