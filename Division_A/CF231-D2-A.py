import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp(x = ''):
    return(int(input(x)))
def inlt(x = ''):
    return(list(map(int,input(x).split())))
def insr(x = ''):
    s = input(x)
    return(list(s[:len(s) - 1]))
def invr(x = ''):
    return(map(int,input(x).split()))

def main():
    n = inp('enter games')
    x = []
    x.append(inlt(f'input game {i}') for i in range(n))
    
    res = 0
    for game in range(len(x)):
        res += 1 if sum(game) >= 2 else 0

    return res

print(int(input('')))

# print(main())