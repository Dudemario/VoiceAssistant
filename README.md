# Overview
A Voice Assistant to help you with your quarantine needs
## Inspiration
The COVID-19 pandemic has changed many aspects of our lives, including our daily interactions. With no one to talk to, we decided to create an assistant that would keep us company and on track during these monotonous times. 

## What it does
Chester can perform any one of its functions through voice commands. His functions include: telling the current time, telling the current weather, playing a video, playing music, doing mathematical calculations, searching things up on Wikipedia, telling jokes, listing events on your google calendar, telling COVID-19 statistics, and providing verbal therapy. 

## How we built it
Chester was built on python and uses numerous python libraries to perform voice-activated functions. The speech_recognition library uses Google Cloud's speech recognition API to turn audio inputs into string data. When Chester is activated, it will listen to audio coming from your computer's microphone and turn it into a string. Chester will then see if that string matches with any of the programmed voice commands, and if it does, Chester will read the text associated with the function out loud using the pyttsx3 library. Data like weather and time are received through libraries that send API requests and functions like the calculator are performed natively. 

## Challenges we ran into

## What we learned
Throughout this build, we learned a lot about webscraping

## What's next for Chester
In the future, we would like to create a dedicated piece of hardware to run Chester on. We could run the program on a Raspberry Pi, connect high-quality speakers, a microphone, a small display, and enclose the components in a 3D printed case to make Chester just like a real voice assistant. This would allow Chester to run even when your main computer is off. In addition to adding a hardware component, we would also like to add more functions. Adding functions like internet monitoring, reading stock prices, reading new emails, telling a random quote, and reading trivia facts are all avenues that we want to explore in the future. 
