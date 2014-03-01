def minTable(array):
	array2 = [line[::-1] for line in array[::-1]]
	table = [[0] * len(array) for x in range(len(array))]
	table[0][0] = array2[0][0]
	for x in range(0, len(array)):
		for y in range(0, len(array)):
			m = array2[x][y]
			if(x > 0):
				m = min(m, table[x-1][y])
			if(y > 0):
				m = min(m, table[x][y-1])
			table[x][y] = m
	return [line[::-1] for line in table[::-1]]


def v1():
	import Queue
	from collections import defaultdict

	with open("prob82.txt") as f:
		matrix = [[int(x) for x in line.strip().split(",")] for line in f.readlines()]

	size = len(matrix)

	minV = min([x for row in matrix for x in row])
	minV = 0
	visited = defaultdict(lambda: 10**9)
	pq = Queue.PriorityQueue()
	for x in range(size):
		pq.put((0, (x, 0, matrix[x][0])))
	x, y = 0, 0
	while not pq.empty():
		_, (x, y, cost) = pq.get()
		if y == size - 1:
			print x,y
			print cost
			break
		if x + 1 < size:
			v = matrix[x+1][y]
			loc = (x+1, y)

			if visited[loc] > v:
				visited[loc] = v
				pq.put((v + cost, (x + 1, y, cost + v)))
		if y + 1 < size:
			v = matrix[x][y + 1]
			loc = (x, y + 1)
			if visited[loc] > v:
				visited[loc] = v
				pq.put((v + cost, (x, y + 1, cost  + v)))
		if x - 1 >= 0:
			v = matrix[x - 1][y]
			loc = (x - 1, y)

			if visited[loc] > v:
				visited[loc] = v
				pq.put((v + cost, (x - 1, y, cost + v)))



def v3():
	with open("prob82.txt") as f:
		matrix = [[int(x) for x in line.strip().split(",")] for line in f.readlines()]

	size = len(matrix)
	columns = [matrix[x][0] for x in range(size)]
	for col in range(1, size):
		comulative = [matrix[x][col] for x in range(size)]
		for row in range(size):
			columns[row] += comulative[row]
			if row > 0:
				comulative[row] += comulative[row - 1]
		print comulative
	print min(columns)



def main():
    from timeit import Timer
    print Timer('v1()', 'from __main__ import v1').timeit(1)
    print Timer('v3()', 'from __main__ import v3').timeit(1)

main()