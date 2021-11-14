import re
import requests
from lxml import html
from bs4 import BeautifulSoup
import datetime

class Lectio:
	def __init__(self, username : str, password : str, schoolID : str):
		result = self.login(username, password, schoolID)

		# If unsuccesful login
		if not result[0]:
			raise Exception(result[1])

	# Log in to the specified user, and return a True/False (login succesful), and a message for the login
	def login(self, username : str, password : str, schoolID : str = None, loginStatuses : list = None) -> (bool, str):
		if schoolID != None:
			self.schoolID = schoolID
		self.username = username
		self.password = password

		loginURL = f"https://www.lectio.dk/lectio/{self.schoolID}/login.aspx"

		# Start requests session and get eventvalidation key
		session = requests.session()
		result = session.get(loginURL)
		tree = html.fromstring(result.text)
		authenticity_token = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]

		# Create payload
		payload = {
			"m$Content$username": self.username,
			"m$Content$password": self.password,
			"m$Content$passwordHidden": self.password,
			"__EVENTVALIDATION": authenticity_token,
			"__EVENTTARGET": "m$Content$submitbtn2",
			"__EVENTARGUMENT": "",
			"masterfootervalue": "X1!ÆØÅ",
			"LectioPostbackId": ""
		}

		# Perform login
		result = session.post(loginURL, data=payload, headers=dict(referer=loginURL))

		# Getting student id
		dashboard = session.get(f"https://www.lectio.dk/lectio/{self.schoolID}/forside.aspx")
		soup = BeautifulSoup(dashboard.text, features="html.parser")
		studentIDFind = soup.find("a", {"id": "s_m_HeaderContent_subnavigator_ctl01"}, href=True)
		studentClassFind = soup.find("div", {"id" : "s_m_HeaderContent_MainTitle"}).text
		studentClassFind = studentClassFind.split("Eleven ")[1]
		studentClassFind = studentClassFind.split(" - Forside")[0]
		self.name, self.class_ = studentClassFind.split(", ")

		classSchedule = str(soup.findAll("ul", {"class" : "entitylinklistH"})[1])
		classSchedule = classSchedule.split(f'">Alle {self.class_}-elever')[0]
		classSchedule = classSchedule.split('href="')[-1]
		classSchedule = classSchedule.split('">')[0]
		classSchedule = classSchedule.replace("&amp;", "&")
		classSchedule = classSchedule.split("SkemaNy")[1]
		self.classSchedule = "SkemaNy" + classSchedule + "&medlemmer=1"

		if loginStatuses == None:
			loginStatuses = ["Log-in succesfuld", "Forkerte login detaljer"]

		if studentIDFind == None:
			return False, loginStatuses[1]
		self.studentID = (studentIDFind['href']).replace(f"/lectio/{self.schoolID}/forside.aspx?elevid=", '')
		self.session = session
		return True, loginStatuses[0]

	# Refresh the session (by logging in again, with the saved credentials
	def refresh(self) -> (bool, str):
		# Re-login, using the already specified credentials
		return self.login(self.username, self.password)

	def getSchedule(self, week : int = None):
		return Schedule(self, None, week)

	def getClassSchedule(self, week : int = None):
		return Schedule(self, self.classSchedule, week)

	@property
	def ClassSchedule(self):
		return self.getClassSchedule()

	@property
	def Schedule(self):
		return self.getSchedule()


class Schedule:
	def __init__(self, lectio : Lectio, url : str = None, week : int = None):
		self.lectio = lectio
		if url == None:
			url = f"SkemaNy.aspx?type=elev&elevid={self.lectio.studentID}"
		# The url of the schedule
		self.scheduleURL = f"https://www.lectio.dk/lectio/{self.lectio.schoolID}/{url}"

		# Current time in a tuple[year, weekNum, dayOfWeek]
		self.year, self.week, dayOfWeek = datetime.datetime.now().isocalendar()
		if dayOfWeek > 5:
			self.week += 1
		# If a week is specified
		if week != None:
			if week < self.week:
				self.year += 1
			self.week = week

		weekStr = f"&week={self.week}{self.year}"
		self.scheduleURL += weekStr

		self.session = lectio.session
		self.days = []
		self.updateSchedule()

	def updateSchedule(self) -> bool:
		lessons = []
		result = self.session.get(self.scheduleURL)

		soup = BeautifulSoup(result.text, features="html.parser")
		scheduleContainer = soup.findAll('a', {"class": "s2bgbox"})
		names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
		nameIndex = 0
		for schedule in scheduleContainer:
			rows = schedule['data-additionalinfo'].split("\n")

			# Getting the lesson id
			# Get the lesson if normal
			if "absid" in schedule['href']:
				lessonIDSplit1 = schedule['href'].split("absid=")
			elif "ProeveholdId" in schedule['href']:
				lessonIDSplit1 = schedule['href'].split("ProeveholdId=")
			else:
				print("Error")
				return False

			lessonIDSplit2 = lessonIDSplit1[1].split("&prevurl=")
			lessonID = lessonIDSplit2[0]

			# Make a lesson
			lesson = self.Day.Lesson(rows, lessonID)

			# If there are no lessons, or they are on the same date
			# Append the latest lesson to the array
			if len(lessons) == 0 or lesson.date.day == lessons[-1].date.day:
				lessons.append(lesson)
			# If the newest lesson (the one currently being checked)
			# Is not the same date as the previous lesson
			else:
				# Make a Day object (with the lessons) and add it to a list
				# It has to be list(lessons) to make a copy of the lesson list
				day = self.Day(names[nameIndex], lessons[-1].date, list(lessons))
				self.days.append(day)
				nameIndex += 1

				# Clear the array and add the newest lesson
				lessons.clear()
				lessons.append(lesson)
		self.days.append(self.Day(names[nameIndex], lessons[-1].date, lessons))
		return True

	def Today(self, mondayIfWeekend : bool = True, onlyWeekdays : bool = True):
		# ISO starts at Sunday = 0. It's easier if Monday = 0
		todayInt = datetime.datetime.now().isoweekday() - 1

		maxDay = 5 if onlyWeekdays else len(self.days)
		# If the day is within the specified range
		if todayInt < maxDay:
			return self.days[todayInt]

		if mondayIfWeekend:
			return Schedule(self.lectio, week=self.week + 1).days[0]
		else:
			return None

	# Used in for loops, so you can iterate over the days on this week/schedule
	def __iter__(self):
		self.index = 0
		return self

	# Used in for loops, so you can iterate over the days on this week/schedule
	def __next__(self):
		if self.index < len(self.days):
			value = self.days[self.index]
			self.index += 1
			return value
		else:
			raise StopIteration

	# Used to implement Schedule[item]
	def __getitem__(self, item : int):
		if item > len(self.days):
			raise IndexError(f"There are only {len(self.days)} lessons in this day (not {item})")
		return self.days[item]

	class Day:
		def __init__(self, name : str, day : datetime.datetime, lessons : list):
			self.name = name
			self.lessons = lessons

			def lessonSort(elem):
				return elem.start

			self.lessons.sort(key=lessonSort)

			self.date = day.strftime("%d/%m")

			# Define the start and end of the day
			self.start = datetime.datetime.combine(day, self[0].start)
			self.end = datetime.datetime.combine(day, self[-1].end)
			# And the length of the day
			self.length = self.end - self.start

		# Used in for loops, so you can iterate over the lessons on this day
		def __iter__(self):
			self.index = 0
			return self

		# Used in for loops, so you can iterate over the lessons on this day
		def __next__(self):
			if self.index < len(self.lessons):
				value = self.lessons[self.index]
				self.index += 1
				return value
			else:
				raise StopIteration

		# Used to implement Day[item]
		def __getitem__(self, item : int):
			if item > len(self.lessons):
				raise IndexError(f"There are only {len(self.lessons)} lessons in this day (not {item})")
			return self.lessons[item]


		class Lesson:
			def __init__(self, dataRows : list, lessonID : str):
				self.id = lessonID
				# The time will always be in the format "DD/MM/YYYY HH:MM til HH:MM"
				timeStructure = re.compile(r'\d+/\d+-\d{4} \d{2}:\d{2} til \d{2}:\d{2}')
				teamStructure = re.compile('Hold: ')

				# Teacher and room can both be plural, therefore it could have an e/r respectively at the end
				teacherStructure = re.compile('Lærer.*: ')
				roomStructure = re.compile('Lokale.*: ')

				statuses = ["Aflyst!", "Ændret!"]
				titleIndex = 0
				# Check if there is a status
				if dataRows[0] in statuses:
					self.status = dataRows[0]
					# Since there is a status, everything is pushed 1 index back (if time was [1] it is now [2])
					titleIndex = 1

				else:
					self.status = " "

				# Check if there is a title
				# The title will be before the time, so if [titleIndex] is time, there is no title
				self.title = " " if timeStructure.match(dataRows[titleIndex]) else dataRows[titleIndex]

				# Save the time/team/teacher/room, by finding the row where the data is stored
				time = list(filter(timeStructure.match, dataRows))
				team = list(filter(teamStructure.match, dataRows))
				teacher = list(filter(teacherStructure.match, dataRows))
				room = list(filter(roomStructure.match, dataRows))

				self.homework = []
				if "Lektier:" in dataRows:
					for i in range(dataRows.index("Lektier:") + 1, len(dataRows)):
						if dataRows[i] == "":
							break
						self.homework.append(dataRows[i][2:-6])

				self.additional = []
				if "Øvrigt indhold:" in dataRows:
					for i in range(dataRows.index("Øvrigt indhold:") + 1, len(dataRows)):
						if dataRows[i] == "":
							break
						self.additional.append(dataRows[i][2:-6])

				self.note = []
				if "Note:" in dataRows:
					for i in range(dataRows.index("Note:") + 1, len(dataRows)):
						if dataRows[i] == "":
							break
						self.note.append(dataRows[i][2:-6])

				# If list is empty (There is no time, room, teacher) then set value to single space
				time = time[0] if len(time) != 0 else " "
				self.team = team[0].split(":")[1].strip() if len(team) != 0 else " "
				self.teacher = teacher[0].split(":")[1].strip() if len(teacher) != 0 else " "
				self.room = room[0].split(":")[1].strip() if len(room) != 0 else " "

				# Parse the time into a datetime.datetime object
				self.dateStr, start, _, end = time.split(" ")
				day, monthYear = self.dateStr.split("/")
				month, year = monthYear.split("-")
				day, month, year = int(day), int(month), int(year)
				self.date = datetime.datetime(year, month, day)

				# Convert the starting and ending time to actual times
				self.start = datetime.time(int(start.split(":")[0]), int(start.split(":")[1]))
				self.end = datetime.time(int(end.split(":")[0]), int(end.split(":")[1]))

				# The total length of the lesson
				self.length = datetime.datetime.combine(self.date, self.end) - datetime.datetime.combine(self.date, self.start)

			@property
			def JSON(self) -> dict:
				return {"LessonID": self.id, "Status": self.status, "Title": self.title, "Date": self.date.strftime("%d/%m-%Y"), "Start": self.start.strftime("%H:%M:%S"), "End": self.end.strftime("%H:%M:%S"), "Team": self.team, "Teacher": self.teacher, "Room": self.room}

#l = Lectio("iben1899", "Itce5334", "202")




l = Lectio("dani724g", "XzaQt_eeg9#`h<q", "305")
schedule = l.getClassSchedule()

for day in schedule:
	print(f"{day.name} ({day.date}): {day.length}")
	for lesson in day:
		homework = "No homework" if len(lesson.homework) == 0 else "Homework:\n\t\t" + '\n\t\t'.join(lesson.homework)
		print(f"\t{lesson.team}:\n\t{homework}")
	print()

"""
	def getSchools(self):
		result = schools.schools(self)
		return result

	def getExercise(self, ExerciseId):
		result = exercise.exercise(self, self.session, self.schoolID, self.studentID, ExerciseId)
		return result

	def getExercises(self):
		result = exercises.exercises(self, self.session, self.schoolID, self.studentID)
		return result

	def getMessages(self):
		result = messages.messages(self, self.session, self.schoolID, self.studentID)
		return result

	def getMessage(self, MessageId):
		result = message.message(self, self.session, self.schoolID, self.studentID, MessageId)
		return result

	def getStudyProgramme(self):
		result = studyProgramme.studyProgramme(self, self.session, self.schoolID, self.studentID)
		return result

	def getUnreadMessages(self):
		result = unreadMessages.unreadMessages(self, self.session, self.schoolID)
		return result
	
	def getGrades(self):
		result = grades.grades(self, self.session, self.schoolID, self.studentID)
		return result

	def getDashboard(self):
		result = dashboard.dashboard(self, self.session, self.schoolID)
		return result
"""