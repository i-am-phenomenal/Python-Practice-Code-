# array = [1, 2, 3, 5, 1, 5, 9, 1, 2, 8]
# newArray = []

# for element in array: 
#     if element not in newArray: 
#         newArray.append(element)
#     else: 
#         pass


# import asyncio
 
 
# @asyncio.coroutine
# def slow_operation():
#     # yield from suspends execution until
#     # there's some result from asyncio.sleep
 
#     yield from asyncio.sleep(1)
 
#     # our task is done, here's the result
#     return 'Future is done!'
 
 
# def got_result(future):
#     print(future.result())
 
 
# # Our main event loop
# loop = asyncio.get_event_loop()
 
# # We create a task from a coroutine
# task = loop.create_task(slow_operation())
 
# # Please notify us when the task is complete
# task.add_done_callback(got_result)
 
# # The loop will close when the task has resolved
# loop.run_until_complete(task)

# def next(): 
#     i = 1
#     while True:
#         yield i * i
#         i += 1

# for num in next(): 
#     if num > 100: 
#         break
#     print(num)



# counter = 0
# def checkNested(counter, object): 
#     global counter
#     for key, value in object.items(): 
#         if type(value) == dict: 
#             counter += 1
#         else: 
#             pass


# stack = []

# def pushItem(element): 
#     global stack
#     stack.insert(0, element)

# def pop(): 
#     global stack
#     stack.pop(0)

# pushItem(0)
# pushItem(10)
# pushItem(20)
# pushItem(30)

# print(stack)
# pop()
# print(stack)

string = "[()]{[()()]()}"
# string = "[[]][[[][]][]]"
stack = []

def pushItem(element): 
    global stack
    stack.insert(0, element)

def popItem():
    global stack
    stack.pop(0)

def removeSpecifiedBracket(closingBracket, openingBracket): 
    global stack
    for iter in range(0, len(stack)): 
        print(stack[iter], "--> ", closingBracket)
        if stack[iter] == closingBracket:
            print("22222222")
            print(iter, "11111111111111111111")
            exit()
            stack.pop(iter)
            break
        else:
            pass
    # for iter in range(0, len(stack)):
    #     if stack[iter] == openingBracket: 


def checkIfBracketsMatch():
    global string, stack
    for char in string: 
        # if char in "[({":
        #     pushItem(char)
        if char == "[": 
            pushItem(char)
        if char == "{": 
            pushItem(char)
        if char == "(":
            pushItem(char)
        if char == "]": 
            removeSpecifiedBracket("]", "")
        if char == ")": 
            removeSpecifiedBracket(")", "")
        if char == "}": 
            removeSpecifiedBracket("}", "")
    if stack == []:
        print("Brackets are balanced")
    else: 
        print("Not balanced")
        print(stack)

# checkIfBracketsMatch()

def factorial(val): 
    output = 1
    for iter in range(val, 0, -1):
        output = output * iter 
    return output

# print(factorial(0))

def bubbleSort(elements): 
    for iter in range(len(elements) -1, 0, -1):
        for iter1 in range(iter):
            if elements[iter1] > elements[iter]: 
                temp = elements[iter1]
                elements[iter1] = elements[iter]
                elements[iter] = temp
    return elements

def removeDuplicates(elements): 
    formatted = []
    for element in elements: 
        if element not in formatted: 
            formatted.append(element)
        else:
            pass
    return formatted

def maxN(elements, n):
    maxElements = []
    dupsRemoved = removeDuplicates(elements)
    indexToStart = len(dupsRemoved) - n
    for iter in range(indexToStart, len(dupsRemoved)):
        maxElements.append(dupsRemoved[iter])
    print(maxElements) 

def minN(elements, n):
    minElements = []
    dupsRemoved = removeDuplicates(elements)
    for iter in range(0, n):
        minElements.append(dupsRemoved[iter])
    print("Min elements", minElements)

# elements = bubbleSort([2, 8, 4, 1, 1, 2, 7, 3, 8, 2])
# maxN(elements, 4)
# minN(elements, 2)

# elements = [1,2,3, [[]], 5]
# formatted = []
# for ele in elements: 
#     if ele == []:
#         pass
#     else: 
#         formatted.append(ele)
# print(formatted)

def checkIfStrong(number):
    number=str(number)
    sumOfFacts = 0
    for digit in number: 
        sumOfFacts += factorial(int(digit))
    if sumOfFacts == int(number):
        print("Strong")
    else: 
        print("Weak")

# checkIfStrong(15)

def avgWordLength(sentence): 
    sentence = sentence.split(" ")
    sumOfLengths = 0
    for word in sentence:
        sumOfLengths += len(word)
    average = sumOfLengths / len(sentence)
    print(average)
     
# avgWordLength(input())

class Node(): 
    def __init__(self, value): 
        self.value = value
        self.next = None


class LinkedList(): 
    def __init__(self, value=0): 
        self.head = None

    def addNewNode(self, node):
        if self.head is None: 
            self.head = node
        else: 
            last = self.head
            while last.next: 
                last = last.next
            last.next = node

    def addNewNodeAtTop(self, node): 
        if self.head is None: 
            self.head = node
        else: 
            newNode = Node(self.head.value)
            node.next = self.head
            self.head = node

    def printNodes(self): 
        temp = self.head
        while temp: 
            print(temp.value)
            temp = temp.next


# linkedList = LinkedList()
# node = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)
# linkedList.addNewNode(node)
# linkedList.addNewNode(node2)
# linkedList.addNewNode(node3)
# linkedList.addNewNode(node4)
# linkedList.addNewNode(node5)
# linkedList.addNewNodeAtTop(node5)
# linkedList.printNodes()

def rotate(array, k):
    length = len(array)
    rotated = []
    secondHalf = array[(length - k) : length ]
    firstHalf = array[0 : length - k]
    rotated = rotated + secondHalf
    rotated = rotated + firstHalf
    print(rotated)
# a = [1,2,3,4,5] #,6,7,8,9,0]

# rotate(a, 1)

def recursiveFunction(maxValue, recursionCounter): 
    if recursionCounter == maxValue: 
        return
        print(recursionCounter)
    else:
        print(recursionCounter)
        recursiveFunction(maxValue, recursionCounter + 1)

recursiveFunction(10, 0)
