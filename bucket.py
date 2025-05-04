def buckets(orig, length):
	l = orig.split(' ')
	fl = []; c = -1; f = []
	for n in l:
		c += 1
		if (length - c) <= len(n):
			fs = (' ').join(f)
			fl.append(fs)
			f = []; c = -1;
		if (length - c) > len(n):
			f.append(n)
			c += len(n)
		else:
			print(fl); return None
	fs = (' ').join(f)
	fl.append(fs)
	print(fl)

buckets("she sells sea shells by the sea", 10)
buckets("the mouse jumped over the cheese", 7)
buckets("fairy dust coated the air", 20)
buckets("a b c d e", 2)
buckets("really long things", 2)