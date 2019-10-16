class Node:
     def __init__(self, data):
          self.left = None
          self.right = None
          self.data = data

     def insert(self, data):
          if self.data:
            if data < self.data:
              if self.left is None:
                  self.left = Node(data)
                  enterYourChoice()
              else:
                  self.left.insert(data)
            elif data > self.data:

              if self.right is None:
                   self.right = Node(data)
                   enterYourChoice()
              else:
                   self.right.insert(data)
                   enterYourChoice()

          else:
               self.data = data

     def PrintTree(self):
          if self.left:
            self.left.PrintTree()
          print(self.data)

          if self.right:
               self.right.PrintTree()

     def searchTree(self, valueToBeSearched):
          if self.data is None or self.data == valueToBeSearched:
               print(self.data)
               print("value found")
               enterYourChoice()
               return self.data
          elif  valueToBeSearched < self.data:
                # if self.left is None:
                return self.left.searchTree(valueToBeSearched)
          else:
                return  self.right.searchTree(valueToBeSearched)

     def findNextLeftChild(self, parentNode):
         if self.data is None or self.data == parentNode:
              print(self.left.data)
              enterYourChoice()
         else:
              if self.data == parentNode:
                  return self.left.findNextLeftChild(parentNode)
              elif self.data > parentNode:
                  return self.left.findNextLeftChild(parentNode)
              elif self.data < parentNode:
                  return self.right.findNextLeftChild(parentNode)

     def findNextRightChild(self, parentNode):
         if self.data is None or self.data == parentNode:
             print(self.right.data)
             # enterYourChoice()
         else:
            if self.data == parentNode:
               return self.findNextLeftChild(parentNode)
            elif self.data > parentNode:
               return self.findNextRightChild(parentNode)
            elif self.data < parentNode:
               return self.findNextRightChild(parentNode)



def switchStatement(userInput):
     root = Node(10)
     if userInput == 1:
         valueToBeInserted = int(input("Enter the value to be inserted"))
         root.insert(valueToBeInserted)
     elif userInput == 2:
         root.PrintTree()
     elif userInput == 3:
         valueToBeSearched = int(input("Enter the value to be searched"))
         root.searchTree(valueToBeSearched)
     elif userInput == 4:
         parentNode = int(input("Enter the parent whose child is to be found"))
         root.findNextLeftChild(parentNode)
     elif userInput == 5:
         parentNode = int(input("Enter the parent whose child is to be found"))
         root.findNextRightChild(parentNode)


def enterYourChoice():
  print("1. insert")
  print("2. read Tree")
  print("3. search Tree")
  print("4. find next left child")
  print("5. find next right child")
  userInput = int(input("Ener yout choice"))
  switchStatement(userInput)


enterYourChoice()

# root = Node(10)
# root.insert(100)
# root.insert(200)
# root.insert(2)
# root.insert(500)
# root.insert(1)
# root.PrintTree()
# # print("++++++++++++++++")
# # root.PrintTree()
# # valueToBeSearched = int(input("Enter the number to be searched"))
# # root.searchTree(valueToBeSearched)
#
# # root.insert(300)
# # root.insert(400)
# # root.insert(500)
# # root.insert(600)
# # root.insert(700)
# # root.insert(800)
# print("11111111111111")
