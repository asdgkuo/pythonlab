def prStr():
    s="num1: {0} num2: {1} num3: {2}" .format(100,200,300)
    print(s)
    s="num1: {0} num2: {2} num3: {1}" .format(100,200,300)
    print(s)
    s="{0:<10}-kk{1:<10}-{2:<10}".format("banana","apple","orange")
    print(s)
    s="{0:>10}-{1:>10}-{2:>10}".format("banana","apple","orange")
    print(s)
    s="{0:<10.2f}".format(3.141592)
    print(s)
    s="{0:^10.5f}".format(4824.333333)
    print(s)
prStr()