from icecream import ic
from tools.col import myzip
from tools.numbers.simp import add, subtract
from tools.numbers.comp import sumofdigits, ispal


def myziptest():
    it1 = [1, 2, 3]
    it2 = ['a', 'b', 'c']
    result = myzip(it1, it2)
    return result

ic(myziptest())

def addtest():
    return add(2, 2)

ic(addtest())

def subtracttest():
    return subtract(10, 2)

ic(subtracttest())

def sumofdigitstest():
    return sumofdigits(12345)

ic(sumofdigitstest())

def ispaltest():
    return ispal(1221)

ic(ispaltest())

ic("Program Complete")





