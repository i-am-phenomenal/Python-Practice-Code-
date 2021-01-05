words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
sortedDict = {}
for word in words:
    if word not in sortedDict: 
        sortedDict[word] = 1
    else:
        sortedDict[word] = sortedDict[word] + 1


sortedDictKeys = (sorted(sortedDict, key=sortedDict.__getitem__))[::-1]
vals = []
for val in range(k):
    vals.append(sortedDictKeys[val])
print(vals)
