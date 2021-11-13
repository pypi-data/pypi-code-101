from getpass import getpass
from . import CBSaccount


def executeCBScal():
	username = input('CBS username: ')
	password = getpass('Password: ')
	
	myAcc = CBSaccount(username, password)
	myAcc.updateCalendar()

if __name__ == '__main__':
	executeCBScal()