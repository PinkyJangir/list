paisa=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
c=0
l=0
d=0
while i<len(paisa):
	if paisa[i]>=10000000:
		c=c+1
	elif paisa[i]>=100000:
		l=l+1
	else:
			d=d+1
	i=i+1
print('carorpati hai',c)
print('lakhpati h',l)
print('dilwale hai',d)