# a=[9,1,1,9]
# i=0
# while i<len(a):
# 	print(a[i]**2,end='')
# 	i=i+1

list=[1,2,3,4,5,6,7,8,9,10]
a=[]
i=0
while i<len(list):
    j=0
    b=[]
    while j<len(list):
        j+=1
    b.append(list[i])
    b.append(list[i]*list[i])
    a.append(b)
    i+=1
print(a)
