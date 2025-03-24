def hourspassed(hour1, hour2):
	time1 = str(hour1.split(' '))
	time2 = str(hour2.split(' '))
    if time1[4] == ':':  
        rtime1 = int(time1[2])*10 + int(time1[3]) + int(time1[5])/6 + int(time1[6])/60
    else:
        rtime1 = int(time1[2]) + int(time1[4])/6 + int(time1[5])/60
    if time2[5] == ':':
        rtime2 = int(time2[2])*10 + int(time2[3]) + int(time2[5])/6 + int(time2[6])/60
    else:
        rtime2 = int(time2[2]) + int(time2[4])/6 + int(time2[5])/60
    if 'PM' in hour1:
	rtime1 += 12
    if 'PM' in hour2:
	rtime2 += 12
    if rtime2 == rtime1:
	print('No time has passed')
    else:
	ftime = rtime2 - rtime1
	if ftime < 1:
		print(round((ftime * 60), 1), 'Minutes passed')
	else:
		h, m = divmod(ftime, 1)
		print(int(h), 'Hours', round((m * 60), 1), 'Minutes passed')

hourspassed("3:00 AM", "9:00 AM")
hourspassed("2:00 PM", "4:00 PM")
hourspassed("1:00 AM", "3:00 PM")
hourspassed("4:00 PM", "4:00 PM")
hourspassed('2:30 AM', '5:10 PM')
hourspassed('2:35 AM', '2:55 AM')
