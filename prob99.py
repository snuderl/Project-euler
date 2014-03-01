import math
	

st = []
with open("prob99.txt") as f:
	for s in f.readlines():
		a, b = map(int, s.split(","))
		st.append(b * math.log(a))
print max(st), st.index(max(st))

