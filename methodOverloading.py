class add:
	def addit(self,a=None,b=None,c=None):
		d=0
		if(a==None and b==None and c!=None):
			print "only",c
		if(a==None and b!=None and c!=None):
			d=b+c
			print(d)
		if(a!=None and b!=None and c!=None):
			d=a+b+c
			print(d)
		return d
one=add()
e=one.addit(None,3,3)
print e