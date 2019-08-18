
#Driver Code
n=int(input())
primes=[]
for i in range(2,n+1):
	c=0
	for j in range(2,i//2):
		if(i%j==0):
			c+=1
	if(c==0):
		primes.append(i)
count=0
for i in range(1,len(primes)):
	if(primes[i]-primes[i-1]==6):
		count+=1
print(count)