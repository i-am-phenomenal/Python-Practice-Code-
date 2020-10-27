# Write your code here
testCases = int(input())
for i in range(testCases): 
    n, k = input().split(" ")
    k = int(k)
    arr = input().split(" ")
    while k > 0: 
        lastElement = arr[len(arr) - 1]
        for iter in range(len(arr)- 1, 0 , -1): 
            arr[iter] = arr[iter - 1]
        arr[0] = lastElement
        k = k - 1
    print(' '.join(arr))
