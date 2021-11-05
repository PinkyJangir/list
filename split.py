main="the quick brown  brown fox jumped over the lazy dog. the dog slept over the verandah."
i=0
s=main.split()
a= "over"
b= " "
while i<len(s):
	if s[i]==a:
		b=b+" "
	else:
		b=b+s[i]+" "
	i=i+1
print(b)