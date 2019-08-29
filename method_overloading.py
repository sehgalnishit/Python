#method for ooperator overloading

# class Student:
# 	def __init__(self,m1,m2):
#  		self.m1=m1
#  		self.m2=m2

# 	def __add__(self,arg):
#  		s3m1=self.m1+arg.m1
#  		s3m2=self.m2+arg.m2
#  		s3=Student(s3m1,s3m2)
#  		return s3

# 	def __gt__(self,arg1):
#  		m1=self.m1+self.m2
#  		m2=arg1.m1+arg1.m2
#  		if(m1>m2):
#  			return True
#  		else:
#  			return False

# s1=Student(10,20)
# s2=Student(110,12)
# s3=s1+s2
# print('total agregate of subject one:' ,s3.m2)
# if(s2>s1):
# 	print('s2 is bigger')
# else:
# 	print('s1 is bigger')
# print(4+3)

class Student:
	def __init__(self,a,b):
		self.a=a
		self.b=b

	def __add__(self,c):
		s3=self.a+c.a
		s32=self.b+c.b
		s=Student(s3,s32)
		return s
s1=Student(10,20)
s2=Student(5,10)
s3=s1+s2

print "a=",s3.a
print "b=",s3.b