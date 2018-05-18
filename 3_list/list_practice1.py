from math import pi
def squareList(nums):
    return[x**2 for x in nums]

def absList(nums,x):
    return [a for a in nums if abs(a)<x]


def piList(n):
    return [round(pi,i) for i in range(1,n+1)]

print("01",squareList([1,2,3]))
print("02",absList([1,-1,4,-3],3))
print("03",piList(5))