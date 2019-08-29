def main():
	f=open('python.py',"r")
	if f.mode=='r':
		content=f.read()
		print content
	f1=f.readLines()
	for x in f1:
		print x
print "yeye"
if __name__=="__main___":
	main()