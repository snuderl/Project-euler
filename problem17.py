words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

words10 = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

words = { (i+1): x for (i, x) in enumerate(words)}

c = 0
for x in range(1, 1000):
	split100 = x / 100
	split10 = (x / 10) % 10
	split1 = x % 10
	#print x, split100, split10, split1
	
	string = ""
	if split100 > 0:
		string += words[split100] + "hundred"
		if split10 > 0 or split1 > 0:
			string+="and"

	if split10 > 0:
		if split10 == 1:
			string += words[split10 * 10 + split1]
			print string, len(string)
			continue
		string += words10[split10-1]
	if split1 > 0:
		string += words[split1]

	print string, len(string)
	c += len(string)

print c + len("onethousand")