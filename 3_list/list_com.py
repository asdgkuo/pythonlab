nums = [0, 1, 2, 3, 4]
'''squares = []
for x in nums:
  squares.append(x ** 2)
print(squares) # prints [0, 1, 4, 9, 16]
'''
squares = [x*2 for x in nums]
print (squares)

nums = [-2,-1,0,1,2]
ds = [abs(x) for x in nums if abs(x)<2]
print("example2" , ds)

from math import pi
print(pi)
print(round(pi,3))
#str將圓周率改成字串
print("example",[str(round(pi,i)) for i in range(1,6)])