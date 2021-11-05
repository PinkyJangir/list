a=[6,1,3,5, 6,3,1]
i=0
prod=1
b=[ ]
while i<len(a):
	if a[i] not in b:
		prod=prod*a[i]
		b.append(a[i])
	i=i+1
print(prod)
