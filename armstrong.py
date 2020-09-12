num=int(input('Enter no. to check if it is armstrong or not '))
sum=0
temp=num
while temp>0:
	digit=temp%10
	sum=sum+digit**3
	temp=temp//10
if num==sum:
	print('%d is armstrong'%(num))
else:
	print('%d is not armstrong'%(num))