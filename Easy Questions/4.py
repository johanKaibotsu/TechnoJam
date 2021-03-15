def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
def check(ls,n):
	s=sum(ls)
	la=str(s)
	if len(la)==len(set(la)):
		print("YES")
	else:
		print("no")
n=int(input())
ls=[int(i) for i in input().split()]
lp=[]
for i in range(n):
	if (isPrime(ls[i])):
		lp.append(ls[i])
check(lp,n)