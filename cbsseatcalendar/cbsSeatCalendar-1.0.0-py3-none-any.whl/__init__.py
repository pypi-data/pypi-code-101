# Top-level objects and function for command line entry point
from cbsCal.cbsCalendarUpdateClass import CBSaccount


def executeCBScal():
	username = input('CBS username: ')
	password = input('Password: ')
	
	myAcc = CBSaccount(username, password)
	myAcc.updateCalendar()



__version__ = '1.0.0'

