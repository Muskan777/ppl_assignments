L = [2,4,6,12,16,17,20,21]
c = 0
cnt = 0
for i in range(25):
	c = c + 1
	cnt = 0
	for j in L:
		if(c==j):
			cnt = cnt + 1
			continue
	if(cnt == 0):
		print(c)
