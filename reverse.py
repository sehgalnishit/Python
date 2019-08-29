a=12345001
reverse=0
while(a>0):
	remainder=a%10
	reverse=(reverse*10)+remainder
	a=a/10
print reverse