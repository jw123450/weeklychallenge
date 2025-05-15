def timeToEat(t):
	t = '0' + t.lower()
	if len(t) > 10:
		t = t[1:]
	time = int(t[0:2]) + (int(t[3:5])/60)
	if 'p.m.' in t:
		time += 12
	if '12' in t:
		time -= 12
	eat = [7, 12, 19]
	nexttimes = [n for n in eat if n > time]
	if nexttimes:
		untiltime = min(nexttimes, key=lambda n: n - time) - time
	else:
		untiltime = min(eat, key=lambda n: n + 24 - time) + 24 - time
	h, m = divmod(untiltime, 1)
	print(f'[{int(h)}, {round(m*60)}]')

timeToEat("2:00 p.m.")
timeToEat("5:50 a.m.")
timeToEat("12:50 p.m.")
timeToEat("10:20 a.m.")
timeToEat("1:15 a.m.")
timeToEat("9:20 p.m.")