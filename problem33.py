__author__ = 'Matej'

import mathTools


print mathTools.higestCommonDivisor(49,98)

for i in xrange(11,100):
    for x in xrange(10,100):
        print i,x
        if int(i%10)==int(x/10):
            print i ,x
            a = i/10
            b = x%10

            divisor = mathTools.higestCommonDivisor(a,b)

            a=a/divisor
            b=b/divisor


            divisor = mathTools.higestCommonDivisor(i,x)

            a1=i/divisor
            b1 = x/divisor

            if(a==a1 and b==b1):
                print i,x





