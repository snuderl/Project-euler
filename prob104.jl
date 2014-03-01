function fibonaci()
   f1 = BigInt(1)
   f2 = f1
   produce(f1)
   produce(f2)
   while true
    t = f2
    f2 = f1 + f2
    f1 = t
    produce(f2)
   end
end

tailCnt = BigInt(1000000000)


function isPandigital(x::Int64)
    store = zeros(9)
    str = string(x)
    if(length(str) < 9) return false end
    for i=1:9
        ch = str[i]
        if(ch == '0')
            return false
        else
            ind = int(string(ch))
            if(store[ind] == 1) return false end
            store[ind] += 1
        end
    end

    for i=1:9
       if(store[i] != 1) return false end
    end

    return true
end

function isSquare(x::BigInt)

    tail = x % tailCnt
    #println(tail)
    if(tail < 123456789 || !isPandigital(int(tail)))
            return false
    end

    return true

    order = 1 + int(trunc(log10(x)))
    head = int(trunc(x / BigInt(10)^(order - 9)))
    #println(order)
    #println(x, " ", 10^(order - 8), " ", head)
    return isPandigital(head)
end

function isSquare2(x::BigInt)

    tail = x % tailCnt
    println(tail)
    if(tail < 123456789 || !isPandigital(int(tail)))
            return false
    end


    order = 1 + int(trunc(log10(x)))
    head = int(trunc(x / BigInt(10)^(order - 9)))
    println(order)
    println(x, " ", 10^(order - 8), " ", head)
    return isPandigital(head)
end

function fibonaci2(n)
   i = 1
   p = Task(fibonaci())
   while i != n
        consume(p)
    end
    consume(p)
end

function run()
i = 3
f1 = BigInt(1)
f2 = BigInt(1)
while true
        t = f2
        f2 = f1 + f2
        f1 = t
        if i > 500 && isSquare(f2)
                break
        end

        if i % 1000 == 0
                println(i)
        end
        i+=1

end
f2, i

end
