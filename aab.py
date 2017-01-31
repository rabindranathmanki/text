n=input('enter the number')
m=n
a=0
while(m!=0): 
	a=m%10+a*10
	m=m/10
if(n==a):
	print('is a palindrome number')
else:
	print('is not a plindrome number')