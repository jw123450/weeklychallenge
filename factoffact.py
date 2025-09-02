import sys
import time

def factorial(n, cache={}):
    if n in cache:
        return cache[n]
    r = 1
    for i in range(2, n + 1):
        r *= i
    cache[n] = r
    return r

def factoffact(x):
    fr = 1
    for i in range(1, x + 1):
        fr *= factorial(i)
    print(fr)
    form = "{:,}".format(int(len(str(fr))))
    print(form)

def time_function(func, x):
    start = time.time()
    result = func(x)
    end = time.time()
    print(f"{x} took {end - start:.6f} seconds")
    return result


sys.set_int_max_str_digits(factorial(12))
time_function(factoffact, 4)
time_function(factoffact, 5)
time_function(factoffact, 6)
time_function(factoffact, int(input("Crash: ")))
