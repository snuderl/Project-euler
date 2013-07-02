import math,time

#Largest palindrome of 2 3-digit numbers

def generateNumbers(howManyDigit):
	number = math.pow(10,howManyDigit-1)
	loopTo = math.pow(10,howManyDigit)
	while(number<loopTo):
		yield number
		number = int(number+1)

def isPalindrom(number):
	text = str(number)
	i = len(text)
	begining = ""
	end = ""
	if(i%2==0):
		begining = text[0:i/2]
		end=text[i/2:i:]
	else:
		begining= text[0:i/2]
		end = text[(i/2)+1:i:]
	return begining==end[::-1]


start = time.time()
bigest = 0
for n1 in generateNumbers(3):
	for n2 in generateNumbers(3):
		product = n1*n2
		if(product>bigest and isPalindrom(product)):
			bigest = product

print bigest
print "Time:", (time.time()-start)
