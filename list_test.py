from list import DifferencesBetweenList
from solution import solution
import random

def random_list():
  return list(set([random.randint(1, 10) for i in range(random.randint(1, 10))]))

def test_1():
  assert DifferencesBetweenList([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]) == [1, 3, 5, 6, 8, 10]
  
def test_2():
  assert DifferencesBetweenList([1, 2, 4, 5, 6, 7], [1, 2, 3, 7, 10]) == solution([1, 2, 4, 5, 6, 7], [1, 2, 3, 7, 10])
  
def test_3():
  a = random_list()
  b = random_list()
  assert DifferencesBetweenList(a, b) == solution(a, b)
  
def test_4():
  a = random_list()
  b = random_list()
  assert DifferencesBetweenList(a, b) == solution(a, b)
  
def test_5():
  a = random_list()
  b = random_list()
  assert DifferencesBetweenList(a, b) == solution(a, b)
  
def test_6():
  a = random_list()
  b = random_list()
  assert DifferencesBetweenList(a, b) == solution(a, b)
