from datetime import datetime


def shortMonthString(month: int):
    shortMonthStrings = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    return shortMonthStrings[month-1]


def shortStringFormat(date: datetime):
    return str(date.day) + shortMonthString(date.month) + str(date.year)
