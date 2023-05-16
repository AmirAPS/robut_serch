
import wikipedia
import pyttsx3 as pt
pt.speak('Hello, welcome to APS Researcher Robot')
while True:
       qw = input('waths the serch?')
       qa = wikipedia.summary(qw)
       print(qa)

       sa = input('Do you want to exit? yes or no?')
       if (sa == 'yes'):
        break
