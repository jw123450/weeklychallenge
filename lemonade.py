def lemonade(nums):
	fives = 0
	tens = 0
	for n in nums:
		if n == 5:
			fives += 1
		elif n == 10:
			if fives < 1:
				print(False); return None
			fives -= 1; tens += 1
		elif n == 20:
			if (tens > 0) & (fives > 0):
				tens -= 1; fives -= 1
			elif fives >= 3: 
				fives -= 3
			else:
				print(False); return None
	print(True)
lemonade([5, 5, 5, 10, 20])
lemonade([5, 5, 10, 10, 20])
lemonade([10, 10])
lemonade([5, 5, 10])