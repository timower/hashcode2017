import math

def get_divisors(n):
    ret = set()
    for d in range(1, int(math.ceil(math.sqrt(n)))):
            if n % d == 0:
                ret.add(d)
                ret.add(n//d)
    return ret

def check_slice(start, end):
    size = (end[0] - start[0] + 1) * (end[1] - start[1] + 1)
    if size > H:
        return False

    mush = 0
    tom = 0
    for r in range(start[0], end[0]+1):
        for c in range(start[1], end[1]+1):
            if pizza[r][c] == 0:
                mush += 1
            else:
                tom += 1
            if mush > L and tom > L:
                return True
    return False
    

def get_slices(r, c):
    ret = []
    return ret

P = input().split(' ')

R = int(P[0])
C = int(P[1])
L = int(P[2])
H = int(P[3])

pizza = []
for i in range(R):
    line = input()
    pizza.append(list(map(lambda c: 0 if c == 'M' else 1, line)))
#print(pizza)

divs = get_divisors(H)
print(divs)



for r in range(R):
    for c in range(C):
        slices = get_slices(r, c)

