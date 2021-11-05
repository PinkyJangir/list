n=[50,40,23,70,56,12,5,10,7]
i=0
max=n[0]
smax=n[0]
tmax=n[0]
while i<len(n):
	if n[i]>max:
		max=n[i]
	j=0
	while j<len(n):
		if max>n[j] and smax<n[j]:
			smax=n[j]
		j=j+1
	k=0
	while k<len(n):
		if smax>n[k] and tmax<n[k]:
			tmax=n[k]
		k+=1
	i=i+1
print(tmax)