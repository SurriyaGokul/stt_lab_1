# Bad Python file with many fundamental pylint errors

import os
import random
import math, sys   # multiple imports on one line, some unused

x = 10
y = "20"  # wrong type usage

def add(a, b, c, d):   # too many args, no docstring
    result = a + b
    if a > 5:
        return result
        print("This will never run")  # unreachable code

def broken_function(): # no return, wrong indentation
  val = 5
   val2 = 10   # bad indentation
  return val + val2

def shadow():
    list = [1,2,3]  # shadows built-in 'list'
    str = "hello"   # shadows built-in 'str'
    return list, str

class badclass:  # lowercase, no docstring
  def __init__(self, name):
      self.name = name
      self.age = 25
      self.temp = math.sqrt(100)  # stored but never used

  def sayhi(self):
      print("hi my name is " + self.name)
      return  # returns nothing

def main():
    add(1, 2, 3, 4)
    broken_function()
    shadow()
    p = badclass("Alice")
    p.sayhi()
    unused_var = os.getcwd()  # never used
    print(x + y)  # type error: int + str

main() # no __name__ guard
