def timeConversion(time):

    if time[:2] == "12" and time[-2:] == "AM":
        return "00" + time[2:-6]
    elif time[:2] == "12" and time[-2:] == "PM":
        return time[:-6]
    elif time[-2:] == "AM":
        return time[:-6]
    else:
        return str(int(time[:2]) + 12) + time[2:5]


def test_TimeConversion():
    print(timeConversion("08:05:00 PM"))
    print(timeConversion("12:05:00 AM"))
    print(timeConversion("07:05:00 AM"))
    print(timeConversion("07:05:00 PM"))


test_TimeConversion()
