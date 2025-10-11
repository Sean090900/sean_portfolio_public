# Creator: Sean Dickson

class LeafNode():

    def __init__(self, character, frequency):
        """
        This class is used to build leaf nodes for a Huffman Encoding Tree
        """
        self.character = character
        self.frequency = frequency
        self.right = None 
        self.left = None