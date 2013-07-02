


def isPalindrome(x):
	i = str(x)
	if(len(i)%2==0):
		return i[0:len(i)/2]==i[len(i)/2:len(i)][::-1]
	else:
		return i[0:len(i)/2]==i[len(i)/2 +1:len(i)][::-1]

c=0
s = 0
import mathTools
for i in xrange(1,10**6):
	if isPalindrome(i):
		if isPalindrome(mathTools.baseConvert(i,2)):
			c+=1
			s=s+i
			print i
print c
print s