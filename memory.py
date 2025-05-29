def actualMemorySize(origsize):
	origsize = origsize.replace('GB', ' GB')
	origsize = origsize.replace('MB', ' MB')
	oslist = origsize.split(' ')
	if 'GB' in origsize:
		size = round((float(oslist[0]) * 0.93), 3)
	elif 'MB' in origsize:
		size = int(round(float(oslist[0]) * 0.93, 0))
	if size < 1:
		size = int(1000 * size) #fake news, it is 1024 MB per GB I think, but close enough
		oslist[1] = 'MB'
	size = str(round(size, 2)) + oslist[1]
	print(size)

actualMemorySize("32GB")
actualMemorySize("2GB")
actualMemorySize("512MB")
actualMemorySize("1.1GB")
actualMemorySize("1.01GB")