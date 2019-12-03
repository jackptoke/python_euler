def breakingRecords(scores):
	c_best = 0
	c_worse = 0
	min, max = scores[0], scores[0]

	for n in scores:
		if n < min:
			c_worse += 1
			min = n
		if n > max:
			c_best += 1
			max = n
	return [c_best, c_worse]


print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))