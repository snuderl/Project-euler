def v1():
	import Queue
	from collections import defaultdict

	with open("prob83.txt") as f:
		matrix = [[int(x) for x in line.strip().split(",")] for line in f.readlines()]

	size = len(matrix)

	minV = min([x for row in matrix for x in row])
	minV = 0
	visited = defaultdict(lambda: 10**9)
	pq = Queue.PriorityQueue()
	for x in range(1):
		pq.put((0, (x, 0, matrix[x][0])))
	x, y = 0, 0
	while not pq.empty():
		_, (x, y, cost) = pq.get()
		if y == size - 1 and x == size - 1:
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
		if y - 1 >= 0:
			v = matrix[x][y - 1]
			loc = (x, y - 1)
			if visited[loc] > v:
				visited[loc] = v
				pq.put((v + cost, (x, y - 1, cost  + v)))
		if x - 1 >= 0:
			v = matrix[x - 1][y]
			loc = (x - 1, y)

			if visited[loc] > v:
				visited[loc] = v
				pq.put((v + cost, (x - 1, y, cost + v)))


def main():
    from timeit import Timer
    print Timer('v1()', 'from __main__ import v1').timeit(1)				

main()