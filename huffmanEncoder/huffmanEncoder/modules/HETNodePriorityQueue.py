# Creator: Sean Dickson

class HETNodePriorityQueue():
    
    def __init__(self):
        """
        This class is used to build a Priority Queue.
        """
        self.queue = []

    def length(self):
        """
        Calculates the current length of the Priority Queue
        :return: The length of the Priority Queue as an int
        """
        return len(self.queue)

    def isEmpty(self):
        """
        Determines if the priority queue is currently holding any items.
        :return: True if the priority queue currently has no items, False otherwise
        """
        if self.queue == []:
            return True
        else:
            return False

    def enqueue(self, node):
        """
        Adds a node to the Priority Queue and sorts appropriately
        :param node: The node to add to the Priority Queue
        """
        self.queue.append(node)
        self.insertionSort()
        
    def dequeue(self):
        """
        Removes item from the front of the Priority Queue and returns it
        :return: The current item from front of the Priority Queue
        """
        if not self.isEmpty():
            item = self.queue[0]
            self.queue = self.queue[1:]
            return item
        else:
            raise Exception('Priority Queue is empty! Cannot delete...')
        
    def insertionSort(self):
        """
        Sorts HET nodes in ascending order via the insertion sort algorithm
        """
        for i in range(self.length()):
            j = i
            while j > 0 and self.queue[j].frequency < self.queue[j-1].frequency:
                temp = self.queue[j]
                self.queue[j] = self.queue[j-1]
                self.queue[j-1] = temp
                j -= 1
