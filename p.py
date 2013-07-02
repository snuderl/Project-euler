import mathTools,time
start = time.time()
for i in xrange(11,100):
    for x in xrange(11,100):
        if (i%10)==(x/10) and not x%10== 0 and not i==x:
            a = i/10
            b = x%10


            divisor = mathTools.higestCommonDivisor(a,b)

            a=a/divisor
            b=b/divisor


            divisor = mathTools.higestCommonDivisor(i,x)

            a1=i/divisor
            b1 = x/divisor

            if(a==a1 and b==b1):
                print a1,b1


print time.time()-start