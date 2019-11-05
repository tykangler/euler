# Although the problem description says to consider only the terms that 
# DO NOT EXCEED a given value, I have designed all these functions to 
# consider UP TO the given value by mistake. To account for that, all inputs
# will be decremented by 1.  

import sys
from math import log, sqrt, floor

# HELPERS -------------

def rec_range(init, max_fib, rform):
   """
   recursive range generator. f0 assumed to be 0. 
   range returned is [0, max_fib]
   rform is applied to f0 and f1 to get fn. rform should be a 
   function accepting two parameters such that rform(f0, f1) => fn
   """
   prev, curr = 0, init
   yield prev
   while curr <= max_fib:
      yield curr
      prev, curr = curr, rform(prev, curr)

def get_phi():
   return (1 + sqrt(5)) / 2

def get_psi():
   return (1 - sqrt(5)) / 2

def floor_epsilon(number):
   return floor(round(number, 5))

def fib_index(fn):
   """
   returns the position in the fibonacci sequence where fn can be found, if fn 
   is at an even position. If fn is not a fibonacci number or is at an odd position, 
   then a float is returned. No attempt is made at rounding.
   fn is a fibonacci number if (5 * fn^2 - 4) is a perfect square. 
   The fibonacci sequence is indexed like so:
   [F0 = 0, F1 = 1, F2 = 1, F3 = 2, ..., fn]
   """
   phi = get_phi()
   return log((fn * sqrt(5) + sqrt(5 * fn ** 2 + 4)) / 2, phi)

# END HELPERS --------------------------------

def fib(max_fib):
   """
   returns the fibonacci sequence with fn <= max_fib
   """
   return [val for val in rec_range(1, max_fib, lambda x, y: x + y)]

def brute(max_fib):
   """
   returns the sum of all even numbers in the fibonacci sequence with fn <= max_fib
   """
   return sum(rec_range(2, max_fib, lambda x, y: x + y * 4))

def mathy(max_fib):
   """
   returns the sum of all even numbers in the fibonacci sequence with fn <= max_fib
   """
   phi = get_phi()
   psi = get_psi()
   floored_index = floor_epsilon(fib_index(max_fib))
   k_power = floored_index // 3
   geometric_sum = lambda fac : (1 - fac ** (3 * k_power + 3)) / (1 - fac ** 3)
   return int((geometric_sum(phi) - geometric_sum(psi)) / sqrt(5))

def test(iterations):
   for i in range(0, iterations):
      if mathy(i) != brute(i):
         return (False, i)
   return (True, i)

dispatch = {'mathy': mathy, 'brute': brute}

def solve(max_fib, func):
   return dispatch[func](max_fib - 1) 