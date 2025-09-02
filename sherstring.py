def isValid(s):
	d, check, l, bozo, saved = {}, [], 0, 0, ''
	for c in s:
		if c not in check:
			check.append(c)
			d[c] = 1
		else:
			d[c] += 1
	avg = len(s) / len(check)
	for b in d:
		if (d[b] > avg) & (bozo != 1):
			d[b] -= 1
			bozo = 1
		l = d[b] + l
		if (d[b] == saved) or (d[b] == d[next(iter(d))]):
			continue
		else:
			print(False)
			return None
		saved = d[b]
	print(True)


isValid("abc") #yynnny
isValid("abcc") 
isValid("abccc")
isValid("aabbcd")
isValid("aabbccddeefghi")
isValid("abcdefghhgfedecba")