def happyYear(year):
	year += 1
	y = str(year)
	while len(y) != len(set(y)):
		year += 1
		y = str(year)
	print(year)		
				
happyYear(2017)
happyYear(1990)
happyYear(2021)
happyYear(22551)
happyYear(21)
happyYear(212221)
happyYear(2001)
