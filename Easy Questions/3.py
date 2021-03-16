def change(ls,n):
	e=0
	for i in range(n):
		if ls[i]%2==0:
			e+=1
	if e==n:
		print(-1)
	elif e<n:
		print(e)
t=int(input())
for _ in range(t):
	n=int(input())
	ls=[int(i) for i in input().split()]
	change(ls,n)