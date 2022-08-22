def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

n, h = invr()
a = list(invr())

maxWidth = n
for height in a:
    if height > h:
        maxWidth += 1

print(maxWidth)