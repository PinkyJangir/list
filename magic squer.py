a = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
row1=0
row2=0
row3=0
col1=0
col2=0
col3=0
d1=0
d2=0
while i<len(a):
	row1= row1+a[0][i]
	row2=row2+a[1][i]
	row3=row3+a[2][i]
	col1=col1+a[i][0]
	col2=col2+a[i][1]
	col3=col3+a[i][2]
	d1=d1+a[i][i]
	d2=d2+a[i][2-i]
	i=i+1 
if row1==row2==row3==col1==col2==col3==d1==d2:
	print('magic squar')
else:
	print('not magic squar')