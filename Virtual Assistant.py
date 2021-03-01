#Google Calendar
from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from bs4 import BeautifulSoup
import pickle
import os.path
#Web-scraping
import re
import requests
import subprocess
import urllib.parse
import urllib.request
#Jokes
import pyjokes
#Text to Speech
import pyttsx3
#Speech Recognition
import speech_recognition
#Wikipedia
import wikipedia
#Time
import datetime



def commands(order):
	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	if order[:4] == "play":
		order = order[5:]
		search = urllib.parse.urlencode({"search_query": order})
		videourl = urllib.request.urlopen("https://www.youtube.com/results?" + search)
		results = re.findall(r"watch\?v=(\S{11})", videourl.read().decode())
		clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(results[0]))
		clip2 = "https://www.youtube.com/watch?v=" + "{}".format(results[0])
		title = BeautifulSoup(clip.content, "html.parser")
		yttitle = title.find_all("meta", property="og:title")
		print("Playing " + yttitle[-1]['content'])
		speak.say("Playing" + yttitle[-1]['content'])
		speak.runAndWait()
		subprocess.Popen("echo > " + "path\\to\\mpv.url " + "$'[InternetShortcut]\nURL='" + clip2, shell=True)
		subprocess.Popen("open " + "path\\to\\mpv.url", shell=True)
	elif "time" in order:
		time = datetime.datetime.now().strftime('%I:%M %p')
		print(time)
		speak.say("The time is" + time)
		speak.runAndWait()
	elif "what is" in order and int(order[8]) in nums:
		order = order[8:]
		if "+" in order:
			order = order.split(" + ")
			ans = int(order[0]) + int(order[1])
			print("The answer is " + str(ans))
			speak.say("The answer is " + str(ans))
			speak.runAndWait()
		elif "-" in order:
			order = order.split(" - ")
			ans = int(order[0]) - int(order[1])
			print("The answer is " + str(ans))
			speak.say("The answer is " + str(ans))
			speak.runAndWait()
		elif "x" in order or "*" in order:
			order = order.split(" * ")
			ans = int(order[0]) * int(order[1])
			print("The answer is " + str(ans))
			speak.say("The answer is " + str(ans))
			speak.runAndWait()
		elif "/" in order:
			order = order.split(" / ")
			ans = int(order[0]) / int(order[1])
			print("The answer is " + str(ans))
			speak.say("The answer is " + str(ans))
			speak.runAndWait()
		elif "^" in order:
			order = order.split(" ^ ")
			ans = int(order[0]) ** int(order[1])
			print("The answer is " + str(ans))
			speak.say("The answer is " + str(ans))
			speak.runAndWait()
		else:
			print("I cannot perform this operation")
			speak.say("I cannot perform this operation")
			speak.runAndWait()

	elif "what is" in order or "who is" in order:
		order = order[7:]
		print(wikipedia.summary(order, 1))
		speak.say(wikipedia.summary(order, 1))
		speak.runAndWait()

	elif "joke" in order:
		joke = pyjokes.get_joke()
		print(joke)
		speak.say(joke)
		speak.runAndWait()
	elif "weather" in order:
		api = "d01e438c286074dc9725c473de0d0112"
		urlstart = "http://api.openweathermap.org/data/2.5/weather?"
		place = order.split(" in ")[1]
		url = urlstart + "appid=" + api + "&q=" + place
		info = requests.get(url).json()
		if info["cod"] != "404":
			maininfo = info["main"]
			temp = maininfo["temp"]
			tempC = round(temp - 273.15, 2)
			tempF = round((tempC * 9 / 5) + 32, 2)
			templike = maininfo["feels_like"]
			templikeC = round(templike - 273.15, 2)
			templikeF = round((templikeC * 9 / 5) + 32, 2)
			humid = maininfo["humidity"]
			weather = info["weather"]
			descrip = weather[0]["description"]
			print("The temperature in Celsius is " + str(tempC) + " and in Farenheit it is " + str(tempF))
			print(
				"It feels like " + str(templikeC) + " in celsius and it feels like " + str(templikeF) + " in farenheit")
			print("The humidity is " + str(humid) + "%")
			print("The condition is currently " + str(descrip))
			speak.say("The temperature in Celsius is " + str(tempC) + " / and in Farenheit it is " + str(tempF))
			speak.say(
				"It feels like " + str(templikeC) + " in celsius and it feels like " + str(templikeF) + " in farenheit")
			speak.say("The humidity is " + str(humid) + "%")
			speak.say("The condition is currently " + str(descrip))
			speak.runAndWait()

		else:
			print(" City Not Found ")
	elif "covid" in order:
		months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
				  "November", "December"]
		url = 'https://api.covid19api.com/dayone/country/'
		country = order.split(" in ")[1].split(" ")
		url = url + country.pop(0)
		for i in country:
			url = url + "-" + i
		data = requests.get(url).json()[-1]
		print("Here is the data for COVID-19 in " + order.split(" in ")[1] + " as of " + months[int(data["Date"][5:7])-1] + " "
				+ data["Date"][8:10] + " " + data["Date"][:4] + ":")
		print("Confirmed Cases: " + str(data["Deaths"] + data["Recovered"] + data["Active"]))
		print("Total Deaths: " + str(data["Deaths"]))
		print("Total Recoveries: " + str(data["Recovered"]))
		speak.say("Here is the data for COVID-19 in " + order.split(" in ")[1] + " as of " + months[int(data["Date"][5:7])-1]
				+ " " + data["Date"][8:10] + " " + data["Date"][:4] + ":")
		speak.say("Confirmed Cases: " + str(data["Deaths"] + data["Recovered"] + data["Active"]))
		speak.say("Total Deaths: " + str(data["Deaths"]))
		speak.say("Total Recoveries: " + str(data["Recovered"]))
		speak.runAndWait()
	elif "calendar" in order:
		months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
				  "November", "December"]
		link = ['https://www.googleapis.com/auth/calendar.readonly']
		cred = None
		if os.path.exists('token.pickle'):
			with open('token.pickle', 'rb') as token:
				cred = pickle.load(token)
		if not cred or not cred.valid:
			if cred and cred.expired and cred.refresh_token:
				cred.refresh(Request())
			else:
				flow = InstalledAppFlow.from_client_secrets_file('credentials.json', link)
				cred = flow.run_local_server(port=0)
			with open('token.pickle', 'wb') as token:
				pickle.dump(cred, token)
		calendar = build('calendar', 'v3', credentials=cred)
		now = datetime.datetime.utcnow().isoformat() + 'Z'
		print('Getting the upcoming 10 events')
		eventsraw = calendar.events().list(calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
										orderBy='startTime').execute()
		events = eventsraw.get('items', [])
		if not events:
			print('No upcoming events found.')
		for event in events:
			date = event['start'].get('dateTime', event['start'].get('date'))
			print(months[int(date[5:7])-1] + " " + date[8:] + " " + date[:4], event['summary'])
			speak.say("You are going to " + event['summary'] + " on " + months[int(date[5:7])-1] + " " + date[8:] + " " + date[:4])
		speak.runAndWait()
	elif "therapy mode" in order:
		print("Entering Conversation Mode")
		speak.say("Entering Conversation Mode")
		speak.runAndWait()
		print("How is your day today?")
		speak.say("How is your day today?")
		speak.runAndWait()
		recog.listen(micro)
		print("That's good. What's on your mind?")
		speak.say("That's good. What's on your mind?")
		speak.runAndWait()
		recog.listen(micro)
		print("Hm, I see. That is challenging, but I believe in you. Anything positive?")
		speak.say("Hm, I see. That is challenging, but I believe in you. Anything positive?")
		speak.runAndWait()
		recog.listen(micro)
		print("Oh that's great! I'm proud of you.")
		speak.say("Oh that's great! I'm proud of you.")
		speak.runAndWait()
		recog.listen(micro)
		print("Aw that kind of sucks, I'm sure it will all work out later on.")
		speak.say("Aw that kind of sucks, I'm sure it will get better later on.")
		speak.runAndWait()
		recog.listen(micro)
		print("No Problem, it was great talking to you")
		speak.say("No Problem, it was great talking to you too")
		speak.runAndWait()
		print("Exiting Conversation Mode")
		speak.say("Exiting Conversation Mode")
		speak.runAndWait()


	else:
		speak.say("I didn't quite understand what you said, can you repeat it again?")
		speak.runAndWait()


speak = pyttsx3.init()
voices = speak.getProperty("voices")
speak.setProperty("voice", voices[7].id)
speak.say("This is Chester, how can I help you?")
speak.runAndWait()
recog = speech_recognition.Recognizer()
with speech_recognition.Microphone() as micro:
	command = "hi"
	while True:
		try:
			print("listening")
			listening = recog.listen(micro)
			command = recog.recognize_google(listening)
			command = command.lower()
			if "chester" in command:
				command = command[8:]
				if command == "bye bye":
					break
				commands(command)
		except speech_recognition.WaitTimeoutError:
			pass
		except speech_recognition.UnknownValueError:
			pass
