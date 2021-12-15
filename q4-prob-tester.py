import random
totals = []
for j in range(100000):
	total = 0
	for i in range(33):
		if random.randint(1,3) == 1:
			total += 1
		else:
			total -= 1

	if total <= -5:
		totals.append(1)
	else:
		totals.append(0)
print(sum(totals)/len(totals))