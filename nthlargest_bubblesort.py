# N th Largest using bubble sort

#Bubble sort Technique
arr=list(map(int,input().split()))
N=int(input())
for i in range(N):
	for j in range(i,len(arr)):
		if(arr[i]<arr[j]):
			arr[i],arr[j]=arr[j],arr[i]
print(arr[N-1])
