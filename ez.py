def findBrokenKeys(str1, str2):
	i = 0
	brokenkeys = []
	for s in str2:
		if (s != str1[i]) and (str1[i] not in brokenkeys):
			brokenkeys.append(str1[i])
		i += 1
	print(brokenkeys)

findBrokenKeys("happy birthday", "hawwy birthday")
findBrokenKeys("starry night", "starrq light")
findBrokenKeys("beethoven", "affthoif5")
