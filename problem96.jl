



function empty()
    st = Array(Any, 9, 9);
    s = Set();
    for i in 1:9
        push!(s, i)
    end
    for x=1:9
            for y=1:9
                    st[x, y] = copy(s)
            end
    end
    st
end

function assignValue(field::Array, row::Int64, col::Int64, val::Int64)
    square = field[row, col]
    if(length(square) == 1 && first(square) != val)
        println("Cant assign $val to $row, $col")
        error("Cant assign $val to $row, $col")
        return field
    elseif(length(square) > 1 && !in(val, square))
        println("Cant assign $val to $row, $col")
        error("Cant assign $val to $row, $col.")
        return field
    end

    field[row, col] = val
    ### Remove val from all columns in same row and all rows in column
    for c in 1:9
        field[row, c] = remove(field[row, c], val)
        if(length(field[row, c]) == 1 && typeof(field[row, c]) != Int64)
             field = assignValue(field, row, c, first(field[row, c]))
        end
        field[c, col] = remove(field[c, col], val)
        if(length(field[c, col]) == 1 && typeof(field[c, col]) != Int64)
             field = assignValue(field, c, col, first(field[c, col]))
        end
    end

    r = itrunc((row - 1) / 3)
    c = itrunc((col - 1) / 3)

    for x in r*3 + 1:(r+1)*3
        for y in c*3 + 1:(c+1)*3
            field[x, y] = remove(field[x, y], val)

            if(length(field[x, y]) == 1 && typeof(field[x, y]) != Int64)
                field = assignValue(field, x, y, first(field[x, y]))
            end
        end
    end
    field
end



function remove(set::Set{Any}, val)
    s = setdiff(set, Set(val))
end

function remove(set::Int64, val)
    return set
end

function isFinished(set)
    return sum(map(length, set)) == 81
end

function isValid(set)
    b = true;
    for i in 1:9
        if(length(unique(set[i, :])) != 9 || length(unique(set[:, i])) != 9)
            return false
        end
    end
    b
end

function cp(s)
    s1 = empty()
    for x in 1:9
        for y in 1:9
           s1[x, y] = copy(s[x, y])
        end
    end
    return s1
end

function solve(set)
    if(isFinished(set))
       return set
    end

    tuples = filter(x -> x[2] > 1, map(x -> (x[1], length(x[2])), enumerate(set)))
    tuples = sort(tuples, by=x -> x[2])
    min = first(tuples)
    max = last(tuples)
    y = int(trunc((min[1]-1) / 9) + 1)
    x = int((min[1] - 1) % 9 + 1)
    ss = copy(set[x, y])
    if(ss == Nothing)
            return set
    end

    for possible in ss
        s1 = deepcopy(set)
        assignValue(s1, x, y, possible)
        s2 = solve(s1)

        if(isFinished(s2) && isValid(s2))
            return s2
        end
    end
    return set
end

function processFromString(lines)
    s = empty()
    for y in 1:9
        i = 1
        for x in replace(lines[1 + y], "\n", "")
            x = int(string(x))
            if(x > 0)
                s = assignValue(s, y, i, x)
            end
            i=i+1
        end
    end
    s
end


lines = readlines(open("sudoku.txt"))
function run()
    result = 0
    for grid in 1:50
        s = processFromString(lines[(grid - 1) * 10 + 1:end])

        tic()
        solved = solve(s)
        toc()
        assert(isFinished(solved))
        assert(isValid(solved))
        result += 100 * solved[1,1] + 10solved[1,2] + solved[1,3]
        #show(solved)
        #break
    end
    result
end
