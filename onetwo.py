n=[ 11,2,555,67,999,20]
i=0
b=[]
while i <len(n):
	j=0
	s=' '
	c=str(n[i])
	while j<len(c):
		if (c[j])=='0':
			s+='zero'
		elif(c[j])=='1':
			s+='one'
		elif(c[j])=='2':
			s=s+'two'
		elif(c[j])=='3':
			s=s+'four'
		elif(c[j])=='4':
			s=s+'four'
		elif(c[j])=='5':
			s=s+'five'
		elif(c[j])=='6':
			s=s+'six'
		elif (c[j])=='7':
			s=s+'seven'
		elif (c[j])=='8':
			s=s+'eight'
		elif(c[j])=='9':
			s=s+'nine'
		j+=1
	i=i+1
	b.append(s)
print(b)

	