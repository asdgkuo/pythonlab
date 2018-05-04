import sys

def sum_lines():
    for line in sys.stdin:
        line = line.strip()
        print(line)
        tokens = line.split()
        print(len(tokens))

def sum_lines_exp():
    for line in sys.stdin:
        line = line.strip()
        tokens = line.split()

        total=0
        for i in range(0,len(tokens)):
            total += float(tokens[i])
        print(total)
sum_lines_exp()

