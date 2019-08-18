def binarysearch(arr,key,L,R):
	if(L>R):
		return -1
	else:
		mid=(L+R)//2
		if(key==arr[mid]):
			return 1
		elif(key<arr[mid]):
			return binarysearch(arr,key,L,mid-1)
		else:
			return binarysearch(arr,key,mid+1,R)


#Driver Code
arr=list(map(int,input().split()))
key=int(input())
if(binarysearch(arr,key,0,len(arr)-1)==1):
	print('Element Found')
else:
	print('Not Found')
