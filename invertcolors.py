def invertcolors(RGB):
	invertedcolors = []
	for color in RGB:
		invertedcolors.append(255-color)
	print(invertedcolors)
invertcolors([255, 255, 255])
invertcolors([155, 233, 1])
