from datetime import datetime

def makeordernum():
    num = datetime.today().strftime("%Y%m%d%H%M%S")
    return num


def now():
    now = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    return now