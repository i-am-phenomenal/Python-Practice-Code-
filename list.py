class List(): 
    def __init__(self, size=0): 
        self.size = size
        self.elements = []

    def addNewElement(self, newElement): 
        currentLength = len(self.elements)
        if currentLength < self.size:
            self.elements.append(newElement)
        elif currentLength ==  self.size: 
            self.size = 2 * self.size
            self.elements.append(newElement)
        else:
            pass

    def printList(self):
        print(self.elements)
    
    def printCurrentSize(self): 
        print(self.size)

listObject = List(1)
for iter in range(15):
    listObject.addNewElement(iter)
    listObject.printCurrentSize()

listObject.printList()
# listObject.printCurrentSize()s

    
            
