def spaceMessage(words):
	words = words.replace(']', '[')
	finalstring = ''
	w = words.split('[')
	while '' in w:
		w.remove('')
	for n in w:
		try:
			funny = int(n[0])
			while funny > 0:
				finalstring = finalstring + n[1:]
				funny -= 1
		except ValueError:
			finalstring = finalstring + n
	print(finalstring)
spaceMessage("ABCD")
spaceMessage("AB[3CD]")
spaceMessage("IF[2E]LG[5O]D")
spaceMessage("[3]AB")