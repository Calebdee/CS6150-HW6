import random

n = 10000000
servers = {}
for i in range(n):
	r = 0
	r1 = random.randint(1, n)
	r2 = random.randint(1, n)

	if r1 in servers and r2 in servers:
		if servers[r1] > servers[r2]:
			r = r2
		else:
			r = r1
	elif r1 in servers and r2 not in servers:
		r =  r2
	else:
		r = r1

	if r in servers:
		servers[r] += 1
	else:
		servers[r] = 0

bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
from matplotlib import pyplot as plt
arr = plt.hist(servers.values(), bins=bins)
for i in range(len(bins)-1):
    plt.text(arr[1][i],arr[0][i],str(round(arr[0][i])), rotation=45)
plt.xticks(bins)
plt.title("N=10,000,000 with Server Loads (part b)")
plt.xlabel("Server loads")
plt.ylabel("Count of Servers with Server Load")
plt.show()
