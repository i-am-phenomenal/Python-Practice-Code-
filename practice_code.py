# import math 

# def round_to_nearest(theta): 
#     print("Theta ",theta)
#     floor = math.floor(theta)
#     ceiling = math.ceil(theta)
#     floor_diff = theta - floor 
#     ceiling_diff = ceiling - theta
#     if floor_diff >= ceiling_diff: 
#         return ceiling
#     else: 
#         return floor

# def get_ac(ab, bc):
#     return math.sqrt((ab * ab) + (bc * bc))   

# degree_sign= u'\N{DEGREE SIGN}'
# # ab = int(input())
# # bc = int(input())
# ab = 1 # Expected output 6 
# bc = 10
# ac = get_ac(ab, bc)
# print("AC ", ac)
# mc = ac / 2
# ratio = mc / bc
# print("Inverse ", math.asin(ratio))
# theta = math.degrees(math.asin(ratio))
# round_to_nearest(theta)
# # print(str(round_to_nearest(theta)) + degree_sign)




# x = int(input())
# y = int(input())

# ratio = x / y
# theta = str(round(math.atan(x, y))) + u'\N{DEGREE SIGN}'
# print(theta)
    
# dict = {}
# count = 0
# for ele in list: 
#     for iter in range(0, len(list)):
#         if list[iter] == ele:
#             count += 1

#     dict[ele] = count
#     count = 0

# print(dict)

num1= int( input( "enter smaller number: "))
num2= int( input( "enter larger number: "))
print("here num1<num2")
#code for lcm:
i=num2
while i>=num2:
    if i%num1==0 and i%num2==0:
        print(i, "is lcm of", num1, "and", num2)
        break
    else:
        i+=1