w1=input()
w2=input()
ans=''
if len(w1)<len(w2):
	n=len(w1)
else:
	n=len(w2)
for x in range(n):
	ans+=w1[x] + w2[x]
ans+=w1[n:]+w2[n:]
print(ans)