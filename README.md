# Overview
A Voice Assistant to help you with your quarantine needs
## Inspiration
The COVID-19 pandemic has changed many aspects of our lives, including our daily interactions. With no one to talk to, we decided to create an assistant that would keep us company and on track during these monotonous times. 

## What it does
Chester can perform any one of its functions through voice commands. His functions include: telling the current time, telling the current weather, playing a video, playing music, doing mathematical calculations, searching things up on Wikipedia, telling jokes, listing events on your google calendar, telling COVID-19 statistics, and providing verbal therapy. 

## How we built it
Chester was built on python and uses numerous python libraries to perform voice-activated functions. The speech_recognition library uses Google Cloud's speech recognition API to turn audio inputs into string data. When Chester is activated, it will listen to audio coming from your computer's microphone and turn it into a string. Chester will then see if that string matches with any of the programmed voice commands, and if it does, Chester will read the text associated with the function out loud using the pyttsx3 library. Data like weather and time are received through libraries that send API requests and functions like the calculator are performed natively. We also utilized the request functions to scrape the website and find functions to look for the specific data we needed. 
