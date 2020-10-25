import pandas as pd #for data table stuff
import matplotlib.pyplot as plt #to make plots
from nltk.corpus import stopwords #cleaning up our words
from nltk.tokenize import word_tokenize
import datetime
from datetime import datetime

#import text file
file = open(r'C:\Users\saipr\Desktop\Coding\Python\Mood Diary\Sep to Oct 16.txt', 'r') 
Lines = file.readlines()
Date = []
Mood = []
Level = []
Description = []
stops = set(stopwords.words('english')) #list of stopwords used

#for loop: for every line = mod 0 is mood, mod 1 is description, mod 3 is blank
count = -1
for l in Lines:
    count +=1
    if(count%3 == 0):
        print(l)
        line = l.strip().split("/") #split by slash
        Date.append(line[0]) #append day
        Mood.append(line[1]) #append mood
        #mood level converseion
        if(line[1].strip() == "stressed"):
            Level.append(0)
        elif(line[1].strip() == "sad"):
            Level.append(1)
        elif(line[1].strip() == "tired"):
            Level.append(2)
        elif(line[1].strip() == "ok"):
            Level.append(3)
        else:Level.append(4)
        
    elif(count%3 == 1):
        #description
        tokens = word_tokenize(l) #turn descriptor into word tokens
        filtered = [w for w in tokens if not w in stops] #filter out stop words
        joinedSentence = ' '.join([str(e) for e in filtered]) #list to sentence
        Description.append(joinedSentence) #add to new list
    else: continue

#merge lists into a dataset named data
listOfLists = [Date, Mood, Level, Description]
data = pd.DataFrame(listOfLists).transpose()
data.columns = ['Date', 'Mood', 'Level', 'Description']

#make sure the columns look like normal (head)
print(data.head())

#make a bar chart of moods and export
data['Mood'].value_counts().plot(kind = 'bar')
plt.title('Frequency of Moods')
plt.xlabel('Mood')
plt.xticks(rotation=70)
plt.ylabel('Frequency')
plt.savefig('moodBar.png')
plt.show()
plt.clf() 


#make a line graph of the moods and export
plt.plot(data['Date'], data['Level'])
plt.title('Mood Over Time')
plt.xlabel('Date')
plt.xticks(rotation=70)
plt.ylabel('Mood Level')
plt.savefig('moodLine.png')
plt.show()
plt.clf() 

#merge into one text file and export
allText = " ".join(d for d in data['Description']) #merge all text to one bulk
text_file = open("moodText.txt", "w")
text_file.write(allText)
text_file.close()

#if you want to turn your text file into a word cloud:
#https://www.wordclouds.com/