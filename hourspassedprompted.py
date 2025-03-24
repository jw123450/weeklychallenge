def hourspassed():
    hour1 = input('Starting Time (in HH:MM AM/PM, e.g. 2:12 AM): ')
    hour2 = input('Ending Time (in HH:MM AM/PM, e.g. 4:22 PM): ')
    time1 = str(hour1.split(' '))
    time2 = str(hour2.split(' ')) 
    print(time1[0], time1[1], time1[2], time1[3], time1[4], time1[5])
    print(time2[0], time2[1], time2[2], time2[3], time2[4], time2[5])
    print(time1, time2)      #23456    2345
    if time1[4] == ':':    #12:45 or 1:34 AM/PM
        rtime1 = int(time1[2])*10 + int(time1[3]) + int(time1[5])/6 + int(time1[6])/60
    else:
        rtime1 = int(time1[2]) + int(time1[4])/6 + int(time1[5])/60
    print(rtime1)
    print(time1, time2)
    print(time1[0], time1[1], time1[2], time1[3], time1[4], time1[5])
    if time2[5] == ':':
        rtime2 = int(time2[2])*10 + int(time2[3]) + int(time2[5])/6 + int(time2[6])/60
    else:
        rtime2 = int(time2[2]) + int(time2[4])/6 + int(time2[5])/60
    print(rtime2)
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

hourspassed()