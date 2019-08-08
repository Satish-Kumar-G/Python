instr=list(map(str,input().split(',')))
for ele in instr:
	name,val=ele.split(':')
	l=len(name)
	while(l!=0):
		if(str(l) in val):
			break
		l-=1
	if(l>0):
		print(name[l-1],end="")
	else:
		print('X',end="")
