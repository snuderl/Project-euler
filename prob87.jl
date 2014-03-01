BOUND = 50000000
seen = Set()
B1 = int(sqrt(BOUND))+1
B2 = int(BOUND^(1/3))+1
B3 = int(BOUND^(1/4))+1
p = primes(B1)
for i1 in p
    sq = i1*i1
    for i2 in p
        if i2 > B2 break end
        sq2 = sq + i2 * i2 * i2
        for i3 in p
            if i3 > B3 break end
            s = sq2 + i3*i3*i3*i3
            if(s <= BOUND)
                push!(seen, s)
            end
        end
    end
end
