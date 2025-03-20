def checknumber(number):
	if (len(number) != 14) or (number[0] != '(') or (number[4] != ')') or (number[5] != ' ') or (number[9] != '-'):
		return False
	else:
		return True
print(checknumber('1234916'))
print(checknumber("(123) 456-7890"))
print(checknumber("1111)555 2345"))
print(checknumber("098) 123 4567"))
print(checknumber('(383) 123-8523'))