def overlap(w1, w2):
	c = -1
	for l in w1:
		c += 1
		if l == w2[0]:
			if (w1[c:] in w2) & (c != 0):
				m1 = w1[:c]
				break
			elif (w1[c:] == w2) & (c == 0):
				m1 = ''
				break
	else:
		m1 = w1
	fs = m1 + w2
	print(fs)

overlap("sweden", "denmark")
overlap("honey", "milk")
overlap("dodge", "dodge")
overlap("sballball", "ballsdfc")