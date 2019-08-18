
#Non Recursive Approach

def binarysearch(arr,key,L,R):
	while(L<R):
		mid=(L+R)//2
		if(key==arr[mid]):
			return 1
		elif(key<arr[mid]):
			R=mid-1
		else:
			L=mid+1
	if(L>R):
		return -1

#Driver Code
arr=list(map(int,input().split()))
key=int(input())
if(binarysearch(arr,key,0,len(arr)-1)==1):
	print('Element Found')
else:
	print('Not Found')
