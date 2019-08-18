

#Driver code
n=int(input())
inp=list(map(int,input().split()))

omly this code

pro=1
out=[]
for i in inp:
	pro*=int(i)
for i in inp:
	out.append(pro//int(i))


till here

print(out)