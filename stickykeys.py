def isLongPressed(orig, new):
	e = 1
	for n in new:
		if n in orig:
			try:
				if n == new[e]:
					print(True)
			except IndexError:
				None
		else:
			return(False)
		e += 1


isLongPressed("alex", "aaleex")
isLongPressed("saeed", "ssaaedd")
isLongPressed("leelee", "lleeelee") 
isLongPressed("Tokyo", "TTokkyoh") 
isLongPressed("laiden", "laiden") 