def convertTime(s):
    period = s[-2:]

    hour = int(s[:2])
    minute = s[3:5]
    second = s[6:8]

    if period == "AM":
        if hour ==12:
            hour =0
    else:
        if hour !=12:
            hour +=12

    hour = f"{hour:02}"

    return f"{hour}:{minute}:{second}"

s= "12:01:00 AM"
print(convertTime(s))