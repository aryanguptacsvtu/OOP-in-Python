from functools import lru_cache
import time

@lru_cache(maxsize=None)
def f(n):
    time.sleep(5)
    return n*3

print(f(20))
print("Done for 20.")
print(f(6))
print("Done for 6.")
print(f(15))
print("Done for 15.")
print("\t")

print("These will not wait for 5 sec.:-")
print(f(20))
print("Done for 20.")
print(f(6))
print("Done for 6.")
print(f(15))
print("Done for 15.")
print("\t")

print("Waiting again for 5s:-")
print(f(100))
print("Done for 100.")


'''
"Function Caching" is a technique for improving the performance of a program.

The 'functools.lru_cache' decorator is used to cache the results of a function so that you can reuse the results instead of recomputing them every time the function is called.
'''