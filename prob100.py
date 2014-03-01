from utils import factor, primes

n = 10
while True:
	D = 1 + 2 * n * (n - 1)
	s = int(D ** 0.5)
	if(s * s == D):
		n = float(n)
		b =   (1 + int(s)) / 2
		pr = []
		print n, b, (1 - int(s)) / 2
		break
	n += 1
	if n % 100000 == 0:
		print n


for x in range(2, 10000):
	if int((2 * x * x - 1)**0.5)**2 == x:
		print x + 1

# x = 30
# while True:
# 	D1 = x * x
# 	D2 = (2 * D1 - 1)
# 	if(int(D2** 0.5)**2  == D2):
# 		n = (1 + int(D2 ** 0.5)) / 2
# 		b =   (1 + x) / 2
# 		print x - 30
# 		print n, b
# 		break
# 	x += 1
# 	if x == 10000000:
# 		break