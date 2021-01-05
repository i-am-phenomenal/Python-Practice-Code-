from timeit import timeit

def memoize(function): 
    cache = dict()
    def innerFunction(val): 
        if val in cache: 
            print(cache)
            return cache[val]
        else:
            result = function(val)
            cache[val] = result
            return result
    return innerFunction

def cube(val): 
    return val ** 3

# withoutMemoization = timeit('cube(2)', globals=globals(), number=1)
# memoized = memoize(cube)
# withMemoization = timeit('memoized(2)', globals=globals(), number=1)
# print(withoutMemoization)
# print(withMemoization)
# print(withMemoization > withoutMemoization)

import who_is_on_my_wifi

print(who_is_on_my_wifi.who())