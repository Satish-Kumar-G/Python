inp=int(input())
c=0
count=0
n=2
while(1):
	count=0
	for i in range(2,n-1):
		if(n%i==0):
			count+=1
	if(count==0):
		c+=1
		count=0
	if(c<inp):
		n+=1
	else:
		break
	
print(n)
