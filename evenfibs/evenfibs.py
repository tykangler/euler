import sys

# recursive range generator. f0 assumed to be 0. 
# lim represents highest possible value in recursive range. 
# rform is applied to f0 and f1 to get fn. rform should be a 
# function accepting two parameters such that rform(f0, f1) => fn
def recursive_range(init_value, lim, rform):
   prev, curr = 0, init_value
   while curr < lim:
      yield curr
      prev, curr = curr, rform(prev, curr)

def fib(n):
   for val in recursive_range(1, n, lambda x, y: x + y):
      print(val)

def brute(n):
   sum = 0
   for val in recursive_range(2, n, lambda x, y: x + y * 4):
      sum += val
   return sum

def mathy(n):
   pass

if __name__ == '__main__':
   pass