# n=int(input('enter the nimber'))
# i=1
# sum=0
# while i<n:
# 	if n%i==0:
# 		sum=sum+i
# 	i=i+1
# if n==sum:
# 	print('parfect')
# else:
# 	print('not parfect')

num=[6,7,5,8]
i=0
while i<len(num):
	sum=0
	j=1
	while j<num[i]:
		if num[i]%j==0:
			sum=sum+j
		j=j+1
		
	if sum==num[i]:
		print(num[i])
	i=i+1