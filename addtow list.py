s= ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
m = [10, 20, 56, 45, 36, 20]
i = 0
b=[ ]
while i< len(s):
	   j=s[i] + str(m[i])
	   b.append(j)
	   i= i +1
print(b)
