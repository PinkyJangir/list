l1=[1,2,3,4,5,6]
l2=[2,3,1,0,6,7]
b=[ ]
i=0
while i<len(l1):
	if l1[i] not in l2:
		b.append(l1[i])
	i+=1
print(b)	