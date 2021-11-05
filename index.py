num=[4,6,8,3,9,2,10,22,35,]
i=0
sum=0
while i<len(num):
	pos=num.index(num[i])
	if pos%2==0:
		sum+=num[i]
	i+=1
print(pos)
print(sum)