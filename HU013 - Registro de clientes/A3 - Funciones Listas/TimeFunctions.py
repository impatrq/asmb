from datetime import date, datetime
import calendar

def getWeekDay():  
    my_date = date.today()
    a = calendar.day_name[my_date.weekday()]
    return a.lower()

def getDay():
    return date.today().strftime("%d-%m-%Y")

def getTime():
    return datetime.now().time().strftime("%H:%M:%S")
