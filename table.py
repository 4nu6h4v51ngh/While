print('Enter range of table you want to print')
n1=int(input('Enter no1. to get table '))
n2=int(input('Enter no.2 to get table '))
while n1<=n2:
	i=1
	while i<=10:
		print(n1*i,end=' ')
		i=i+1
	n1=n1+1
	print('\n')