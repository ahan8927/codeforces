import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def main():
    a, b = inlt()
    year = 0
    while a <= b:
        a *= 3
        b *= 2
        year += 1
    return year

print(main())