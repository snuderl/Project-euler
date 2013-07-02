import time

fn = 1
fn_1 = 1
count = 2

while(fn<10**999):
	tmp = fn
	fn = fn + fn_1
	fn_1=tmp
	count+=1
print count
print fn
