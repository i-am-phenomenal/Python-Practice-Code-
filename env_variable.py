# import os 
# import numpy
# import requests
# import sys
# print(sys.path)
# env = os.environ
# print(env["PATH"])
# print(type(env["PATH"]))

# def addPathToEnvVariable(path):
#     PATH = os.environ["PATH"] + ";"
#     PATH = PATH + path
#     os.environ["PATH"]=PATH 

# path  ="C:\Users\ac58833.IND\AppData\Local\Temp\osm-bundler-wc2bcm\pmvs"
# addPathToEnvVariable(path)
# import requests
# from tabpy.tabpy_tools.client import Client
# import tabpy
# client = Client("http://localhost:9004/")

# def multiply_3(x, y): 
#     return x * y
    # import numpy as np
    # return np.sum(x, y).tolist()

# client.deploy('multiply_3', multiply_3, "MULTIPLIES 2 NUMBERS USING NUMPY")
# SCRIPT_REAL("return tabpy.query('multiply',_arg1,_arg2)['response']",-SUM([Col_1]),SUM([Col_2]))
# response = requests.get("http://localhost:9004/multiply_2", headers={"Content-Type": "application/json"})
# print(response.content)
# print("111111111111")
# tabResponse = tabpy.query("multiply_2", 2, 3)
# print(tabResponse)
# import json
# data = json.dumps({"x": 10, "y": 20})
# data = json.dumps({"data": {"x": 11, "y": 20}})
# response = requests.post("http://localhost:9004/query/multiply_3", data=data, headers={"Content-Type": "application/json"})
# print(response.content)


arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [1,2,3,4,5]
arr = [str(x) for x in arr]
k = 5
# lastK = arr[len(arr) - 1 : ((len(arr) - k) - 1) : -1]
# lastK = lastK[:: -1]
# firstK = arr[0 : len(arr) - (k)]
# print(firstK)
# print(' '.join(lastK + firstK))
o = []
for item in range(len(arr) - k, len(arr)):
    o.append(arr[item])
for item in range(0, len(arr) - k): 
    o.append(arr[item])
print(o)