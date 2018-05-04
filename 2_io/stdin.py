import sys

def readLines():
    for line in sys.stdin:
        line = line.strip()  #可消掉輸出的空行
        num = int(line)
        print(num)
readLines()
