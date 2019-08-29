'''map filter wala'''
def check_even(n):
	if n%2==0:
		return True
	else:
		return False

def sumit(a,b):
	return a+b

numbers=[1,2,34,45,2,3,1234,124]

even=list(filter(check_even,numbers))
print('even numbers: ',even)

doubles=list(map(lambda n:n*n,even))
print('this is doubles',doubles)

sumofall=reduce(sumit,doubles)
print('sum:',sumofall)