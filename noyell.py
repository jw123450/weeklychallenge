def noYelling(s):
	n = s[-1]
	while s[-1] == n:
		s = s[:-1]
	s = s+n
	print(s)

noYelling("What went wrong?????????")
noYelling("Oh my goodness!!!")
noYelling("I just!!! can!!! not!!! believe!!! it!!!")
noYelling("Oh my goodness!")