lines = read(open("prob98.txt"))
words = map(x -> replace(x, "\"", ""), split(lines, ","))
