num=30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
a=[ ]
while i<len(n):
         j=i
         b=[ ]
         while j<len(n):
             if n[i]+n[j]==num:
                     b.append(n[i])
                     b.append(n[j])
                     a.append(b)
             j=j+1
         i=i+1
print(a)