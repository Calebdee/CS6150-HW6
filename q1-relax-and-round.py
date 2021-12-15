import random
from scipy.optimize import linprog
import pulp as pl


m = n = 500
d = 25
people = []

for i in range(n):
	skill_i = set()
	while len(skill_i) < d:
		skill_i.add(random.randint(0, m))
	people.append(list(skill_i))
demand_vars = []

prob = pl.LpProblem("LSCP", pl.LpMinimize)
#Objective

trav = 0
var = {}
for peo in people:
	var[trav] = pl.LpVariable("x"+str(trav), lowBound = 0)

prob += [1]*m
for i in range(m):
	prob += var[i] >= 0
	prob += var[i] <= 1

prob.solve()

# c = [1]*n
# bounds = [(0,1) for i in range(m)]
# print(len(people))
# linprog(c, bounds=bounds)
