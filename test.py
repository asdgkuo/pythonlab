print("hello world")
print("hello","world")
print("hello","world",sep="-")
#sep可在字與字的中間加東西
#end可在字串後加東西 不會換行 例題如下
print("hello",end="@")
print("abc")

#運算

#整數除法
print(9//2)
#餘數
print(9%5)
#次方
print(3**3)

#變數宣告

a = 1
b = 2
print(a + b)

str="the color of apple is red"
print(str)
print(len(str))
print(str[::-1])
print(str[:])
print(str[3:])
print(str[3:10])
print(str[:5])

print("{0} {5}".format(100,200))
print("num1:{1} num2:{2}" .format(a,b))
print("{0:10} {1:10}".format(100,200))
print("{0:<7} {1:<7} {2:<7}".format(100,200,3000))
print("{0:>7} {1:>7} {2:>7}".format(1000,20000,2000)")