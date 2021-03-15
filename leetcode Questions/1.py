def xO(start,n):
    xor = start
    for i in range(1,n):
        xor = xor ^ (start+2*i)
    return xor
n=int(input())
start=int(input())
print(xO(start,n))
