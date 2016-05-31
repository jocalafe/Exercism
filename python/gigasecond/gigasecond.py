import datetime

def add_gigasecond(dob):
    gsd = datetime.datetime(dob.year, dob.month, dob.day, dob.hour, dob.minute, dob.second)
    return gsd + datetime.timedelta(seconds = 10**9)
