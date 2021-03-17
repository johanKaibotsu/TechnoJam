def fight(ls,n,Q):
	k=0
	for i in range(n):
		if ls[i]=='1':
			k-=1
		if ls[i]=='0':
			k+=1
	if k<4 and k>-4:
		print(Q[k])
	else:
		print(Q[k%4])
Q=['tywin','hound','jaime','mountain']
t=int(input())
for _ in range(t):
	n=int(input())
	ls=str(input())
	fight(ls,n,Q)
