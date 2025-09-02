def birthdayCakeCandles(l):
	counter = 0
	if not l:
		print("0"); return None
	t = max(l)
	for n in l:
		if n == t:
			counter += 1
	print(counter)

birthdayCakeCandles([4,4,1,3])
birthdayCakeCandles([1, 1, 1, 1])
birthdayCakeCandles([])