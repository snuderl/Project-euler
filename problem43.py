'''
Problem 43
09 May 2003

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''



S = []



def pandigital(n):
	first = range(1,10)
	l = []
	for x in first:
		comb(str(x),n,[0]+[a for a in first if x!=a])
	return l

def comb(c,n,l):
	if(isValid(c)):
		if(len(c)==n):
			S.append(int(c))
		else:
			g=[]
			for x in l:
				a = c+str(x)
				if(isValid(a)):
					comb(c+str(x),n,[a for a in l if a!=x])
			return g

def isValid(c):
	if(len(c)==4):
		n = int(c[1:])
		if n%2==1:
			return False

	if(len(c)==5):
		n=int(c[2:])
		if not n%3==0:
			return False
	if(len(c)==6):
		n=int(c[3:])
		if not n%5==0:
			return False
	if(len(c)==7):
		n=int(c[4:])
		if not n%7==0:
			return False
	if(len(c)==8):
		n=int(c[5:])
		if not n%11==0:
			return False
	if(len(c)==9):
		n=int(c[6:])
		if not n%13==0:
			return False
	if(len(c)==10):
		n=int(c[7:])
		if not n%17==0:
			return False

	return True
import time
start = time.time()
pandigital(10)
print sum(S)
print time.time()-start