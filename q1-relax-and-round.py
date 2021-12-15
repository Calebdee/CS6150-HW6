import random

m = n = 500
d = 25
people = []

for i in range(n):
	skill_i = set()
	while len(skill_i) < d:
		skill_i.add(random.randint(0, m))
	people.append(skill_i)
	print(skill_i)
