def censor(wordsrtring):
	finalwords = []
	words = wordsrtring.split(' ')
	for word in words:
		thing = ''
		counterthing = len(word)
		if counterthing > 4:
			while counterthing > 0:
				thing = thing + '*'
				counterthing -= 1
			finalwords.append(thing)
		if len(word) <= 4:
			finalwords.append(word)
	finalstring = " ".join(finalwords)
	print(finalstring)

censor("The code is fourty")
censor("Two plus three is five")
censor("aaaa aaaaa 1234 12345")
censor('      ')