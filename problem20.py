import math,time 
start=time.time()

fact = math.factorial(100)
x = sum([int(x) for x in str(fact)])
print x
print time.time()-start
