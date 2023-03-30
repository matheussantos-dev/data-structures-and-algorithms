class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, element):
        newNode = Node(element)
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newNode

        self.size = self.size + 1

    def remove(self, element):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value is element:
                if currentNode is self.head:
                    self.head = currentNode.next                   
                else:
                    prev.next = currentNode.next 
                currentNode = None
                self.size = self.size - 1    
                break
            prev = currentNode
            currentNode = currentNode.next   

    def printList(self):
        if self.head is None:
            print('Empty')
        else:    
            currentNode = self.head    
            while currentNode is not None:
                print(currentNode.value)                               
                currentNode = currentNode.next
   