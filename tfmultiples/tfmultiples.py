import sys

def brute(n):
   return sum([val for val in range(1, n) 
               if val % 3 == 0 or val % 5 == 0])

def mathy(n):
   mult_sum = lambda bound : \
      bound * (((n - 1) // bound) ** 2 + ((n - 1) // bound)) // 2
   return mult_sum(5) + mult_sum(3) - mult_sum(15)

dispatch = {'mathy': mathy, 'brute': brute}

def solve(n, func):
   return dispatch[func](n)