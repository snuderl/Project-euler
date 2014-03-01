v1 = collect((-175, 41))
v2 = collect((-421, -714))
v3 = collect((574, -645))

lines = map(x -> map(float, split(replace(x, "\n", ""), ",")), readlines(open("prob102.txt")))
triangles = map(collect, lines)

function containsOrigin(v1, v2, v3)
    v2 = v2 - v1
    v3 = v3 - v1

    x, y = -v1
    x1, y1 = v2
    x2, y2 = v3

    top = y*x1 - x * y1
    bot = y2 * x1 - y1 * x2

    b = top / bot
    a = (x - b * x2) / x1

    if(a > 0 && a < 1 && b > 0 && b < 1 && a + b < 1)
        return 1
    else
        return 0
    end
end

function run()
    s = 0
    for each in triangles
        v1 = each[1:2]
        v2 = each[3:4]
        v3 = each[5:6]

        s += containsOrigin(v1, v2, v3)
    end
    s
end
