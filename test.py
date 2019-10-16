# list = []
# minimum = ''
# for iter in range(0, 5):
#     element = input("Enter the element")
#     list.append(element)
#
# for iterator in range(0, len(list)):
#     for iter in range(0, len(list)):
#         currentCounter = iterator
#         nextCounter = iter
#         print("1111", list[currentCounter])
#         print("+++", list[nextCounter])
#         if list[currentCounter] <= list[nextCounter]:
#             minimum = list[currentCounter]
#         else:
#              pass
#
# print(minimum)
#  global dict
#     global currentCounter
#     listOfValues = files.values()
#     listOfKeys = files.keys()
#     for ele in listOfValues:
#         dict = {ele: listOfValues[currentCounter]}
#         currentCounter = currentCounter + 1

# forward = []
# backward = []
#
# def checkIfPallindrome(word):
#     global forward
#     global backward
#     for char in word:
#         forward.append(char)
#
#     print(word[len(word) - 1])
#
#     for iter in range((len(word) - 1), 0, -1):
#         backward.append(word[iter])
#
#     print(forward)
#     print(backward)
#
#     if forward == backward:
#         return  True
#     else:
#          return False
#
# print(checkIfPallindrome('NITIN1'))

# x = set()
# print(x)
# def checkSpeed(speed):
#     if speed <= 70:
#         print("Ok")
#         return
#     else:
#         points = int((speed % 70) / 5)
#         print("Points: ",points)
#         if points >= 12:
#             print("License suspended")
#
# speed = int(input("Enter the speed of the driver"))
# checkSpeed(speed)
# def calculateSum(limit):
#     listOfNumbers = []
#     sum = 0
#     for num in range(0, (limit + 1)):
#         if (num % 3) == 0 or (num % 5) == 0:
#             listOfNumbers.append(num)
#     print(listOfNumbers)
#
#     for ele in listOfNumbers:
#         sum = sum + ele
#     print("SUm = :", sum)
#
# limit = int(input("enter the limit"))
# calculateSum(limit)
# def lone_sum(num1, num2, num3):
#     # numbersList = [num1, num2, num3]
#     # for ele in numbersList:
#     #     for iter in range(1, len(numbersList)):
#     #         if ele == numbersList
#     if num1 == num2:
#         return num3
#     elif num2 == num3:
#         return num1
#     elif num1 == num3:
#         return num2
#     elif (num1 == num2 and num1 == num3) or (num2 == num1 and num2 == num3) or (num3 == num1 or num3 == num2):
#         return 0
#     else:
#         return (num1 + num2 + num3)
#
#
# num1 = int(input("Enter number 1"))
# num2 = int(input("Enter number 2"))
# num3 = int(input("Enter number 3"))
#
# sum = lone_sum(num1, num2, num3)
# print(sum)
roundedNumbers = []
sum = 0
floor  = 0
ceiling = 0
def numberRoundUpPositive(number):
    global roundedNumber
    global floor
    if (number % 10) == 0:
        roundedNumbers.append(number)
        floor = number
    else:
        numberRoundUpPositive(number + 1)

def numberRoundUpNegative(number):
    global ceiling
    if (number % 10) == 0:
        ceiling = number
    else:
        numberRoundUpNegative(number - 1)


number = int(input("Enter any number"))
# secondNumber = int(input("Enter any number"))
# thirdNumber = int(input("Enter any number"))
numberRoundUpPositive(number)
numberRoundUpNegative(number)
print("Floor", floor)
print("Ceiling", ceiling)
print(int ((floor + ceiling) / 2))
if number <= int ((floor + ceiling) / 2):
    roundedNumbers.append(floor)
else:
    roundedNumbers.append(ceiling)

print(roundedNumbers)
