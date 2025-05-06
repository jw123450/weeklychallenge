def isShuffledWell(l):
	d = l.pop(0); counter = 0
	for n in l:
		if n == (d+1) or n == (d-1):
			counter += 1
		d = n
	if counter >= 3:
		print('Bad Shuffle, do better')
	else:
		print('Good Shuffle!')

isShuffledWell([1, 2, 3, 5, 8, 6, 9, 10, 7, 4])
isShuffledWell([3, 5, 1, 9, 8, 7, 6, 4, 2, 10])
isShuffledWell([1, 5, 3, 8, 10, 2, 7, 6, 4, 9])
isShuffledWell([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])