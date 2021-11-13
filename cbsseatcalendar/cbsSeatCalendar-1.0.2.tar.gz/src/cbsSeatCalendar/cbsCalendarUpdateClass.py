"""
Simple CBS account class with method to add study seat/room bookings to calendar.
Can be run as command line
"""

class CBSaccount:
	def __init__(self, username, password):
		from exchangelib import Credentials, Configuration, Account, EWSTimeZone, DELEGATE
		
		username = username
		password = password
		mailAddress = username + '@student.cbs.dk'
		credentials = Credentials(mailAddress, password)
		
		config = Configuration(credentials = credentials,
		                       server = 'outlook.office365.com')
		self.account = Account(primary_smtp_address = mailAddress,
		                       access_type = DELEGATE,
		                       autodiscover = False,
		                       credentials = credentials,
		                       config = config)
		self.tz = EWSTimeZone('Europe/Copenhagen')

	
	def updateCalendar(self):
		from exchangelib import CalendarItem, EWSDateTime
		import datetime as dt
		
		today = dt.datetime.today().replace(tzinfo=self.tz)
		twoWeeksAgo = today-dt.timedelta(days=15)
		
		# all mails with booking confirmation sent during the last two weeks
		bookingMails = self.account.inbox.filter(f'From:lokaleadm@cbs.dk, '
		                                         f'Sent:{twoWeeksAgo.strftime("%m/%d/%Y")}'
		                                         f'..{today.strftime("%m/%d/%Y")}')
		
		updatedBookings = []
		if bookingMails.count() == 0: # see if there are any mails from the last 15 days
			print('Found no booking mails (from the last 2 weeks) to add to calendar.')
		else: # add bookings to calendar
			for mail in bookingMails:
				if not mail.subject.startswith('Booking Confirmation'):
					continue
				
				if "This booking was for a 'Group Study Room'" in mail.body.splitlines()[8]:
					seatString = 'Room: ' + mail.body.splitlines()[4].strip()[11:]
					seatRoomLocation = seatString[6:]
				elif "This booking was for a 'Single Study Seat'" in mail.body.splitlines()[8]:
					seatString = mail.body.splitlines()[4].strip()[5:-13]
					seatRoomLocation = seatString[6:]
				else:
					seatString = mail.body.splitlines()[4].strip()
					seatRoomLocation = seatString[11:]
				
				dayString, monthString, yearString = mail.body.splitlines()[5].strip().split()[2].split(sep='-')
				timeStartString, timeEndString = mail.body.splitlines()[6].strip().split()[1].split(sep='-')
				
				hourStart = int(timeStartString.split(sep=':')[0])
				minuteStart = int(timeStartString.split(sep=':')[1])
				
				hourEnd = int(timeEndString.split(sep=':')[0])
				minuteEnd = int(timeEndString.split(sep=':')[1])
				
				startdt = dt.datetime(year=int(yearString),
				                      month=int(monthString),
				                      day=int(dayString),
				                      hour=hourStart,
				                      minute=minuteStart).replace(tzinfo = self.tz)
				enddt = dt.datetime(year=int(yearString),
				                    month=int(monthString),
				                    day=int(dayString),
				                    hour=hourEnd,
				                    minute=minuteEnd).replace(tzinfo = self.tz)
				
				# if booking is in the past, break
				yesterday = today - dt.timedelta(days=1)
				if startdt < yesterday:
					continue
				
				startEWS = EWSDateTime.from_datetime(startdt)
				endEWS = EWSDateTime.from_datetime(enddt)
				
				# skip duplicates
				alreadyThere = self.account.calendar.filter(subject=seatString,
				                                            start=startEWS,
				                                            end=endEWS,
				                                            location=seatRoomLocation).all().count() != 0
				
				if alreadyThere:
					pass
				else:
					ev = CalendarItem(folder=self.account.calendar,
					                  subject=seatString,
					                  start=startEWS,
					                  end=endEWS,
					                  location=seatRoomLocation)
					
					ev.save()
					
					updatedBookings.append(f'    {seatString}.  '
					                       f'Time: {startEWS.strftime("%H:%M")}-{endEWS.strftime("%H:%M")}.  '
					                       f'Date: {startEWS.strftime("%d/%m/%Y")}')
			
			if len(updatedBookings) != 0:
				print('Study seats and/or group room bookings added to calendar:')
				print('\n'.join(updatedBookings))
			elif len(updatedBookings) == 0:
				print('Found no new relevant bookings to add to calendar.')




