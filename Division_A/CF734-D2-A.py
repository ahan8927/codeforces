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
    n = inp()
    s = insr()

    Anton = 'Anton'
    Danik = 'Danik'
    Friendship = 'Friendship'

    a = 0

    for i in s:
        if i == 'A':
            a += 1

    d = n - a

    if d < a:
        return Anton
    elif d > a:
        return Danik
    else: 
        return Friendship

print(main())