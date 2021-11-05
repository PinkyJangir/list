a=int(input('enter the number'))
i =1
b=[ ]
while i<=(a):
	j=1
	c=[ ]
	while j<=10:
		c.append(j*i)
		j=j+1
	b.append(i)
	i=i+1
	b.append(c,)
print(b)
