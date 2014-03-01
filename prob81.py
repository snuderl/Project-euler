with open("matrix.txt") as f:
	matrix = [[int(x) for x in line.strip().split(",")] for line in f.readlines()]


size = 80
def v2():

	minimals = [[0] * (size ) for x in range(size)]
	for x in range(0, size):
		for y in range(0, size):
			if x > 0:
				s0 = minimals[x - 1][y]
				m = s0
				if y > 0:
					s1 = minimals[x][y - 1]
					m = min(s1, s0)
			elif y > 0:
				m = minimals[x][y - 1]
			else:
				m = 0
			minimals[x][y] = matrix[x][y] + m
	print minimals[-1][-1]
v2()