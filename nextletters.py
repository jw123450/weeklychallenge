def next_letters(orig):
	b26 = ltob26(orig)
	b26 += 1
	fr = b26tol(b26)
	print(fr)

def ltob26(l):
	result = 0
	for t in l:
		result = (result * 26 + (ord(t) - ord('A'))) + 1
	return result

def b26tol(b26):
	l = ""
	while b26 > 0:
		b26 -= 1
		l = chr(b26 % 26 + ord('A')) + l
		b26 //= 26
	return l




next_letters("A")
next_letters("ABC")
next_letters("Z")
next_letters("CAZ")
next_letters("")