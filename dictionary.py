import pyttsx3
from  PyDictionary import PyDictionary

engine=pyttsx3.init('sapi5')
voices =engine.getProperty('voices')

engine.setProperty('voice',voices[0].id);
#engine.setProperty('voice',voices[1].id);
engine.setProperty('rate',150)

engine.say("Hello Sir, Enter the word for its meaning")
engine.runAndWait()

dict=PyDictionary()

while True:
    query = input("\nEnter Word: ")
    try:
        word=dict.meaning(query)
        for meaning in word:
            print(f"\nMeaning of {query} is {str(word[meaning])}\n")
            engine.say(f"\nMeaning of {query} is {str(word[meaning])}\n")
            engine.runAndWait()
            break

    except:
        print("\nSorry sir,Please Try Again\n")
        engine.say("Sorry sir,Please Try Again")
        engine.runAndWait()

