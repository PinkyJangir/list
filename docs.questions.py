# list=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# i=0
# sum=0
# while i<len(list):
# 	j=0
# 	while j<len(list[i]):
# 		print(list[i][j],end='')
# 		j+=1
# 	i=i+1


a=['1','2','3','4','5','6','7','8','9']
i=1
b=[ ]
while i<len(a):
	j=0
	while j<len(a[j]):
		n=a[i]+a[j]
		b.append(n)
		j=j+1
	i=i+1
print(b)

