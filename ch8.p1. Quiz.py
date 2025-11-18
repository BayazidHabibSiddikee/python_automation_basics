#! python3
# Random quize
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

'''for i in capitals.keys():
     print(i)'''

for quiz in range(35):
    quizefile = open(f'Capital Quize Of America {quiz+1}.txt','w')
    ansfile = open('Capital Quize Of America Answers '+str(quiz+1)+'.txt','w')


    #write header
    quizefile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizefile.write((' '* 20) + f'State Capitals Quiz (Form {quiz+1})')
    quizefile.write('\n\n')

    #Shuffle the order of lists
    states = list(capitals.keys())
    random.shuffle(states)
    
    
    #Lets create answer script well
    for i in range(50):
        correctans = capitals[states[i]]
        wrongans = list(capitals.values())
        del wrongans[wrongans.index(correctans)]
        wrongans = random.sample(wrongans,3)
        ansoption = wrongans + [correctans]
        random.shuffle(ansoption)


        quizefile.write(f'{i + 1}. What is the capital of {states[i]}?\n')
        for j in range(4):
            quizefile.write('ABCD'[j] + '.' + ansoption[j]+'\n')

            
        ansfile.write(str(i+1)+'.'+'ABCD'[ansoption.index(correctans)]+'\n')
    quizefile.close()
    ansfile.close()
            
