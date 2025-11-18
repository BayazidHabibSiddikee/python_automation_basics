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


for i in range(35):  #35 types of quistion
    qF = open(f'Ai Swighat\\Qn Type {i+1} of Capital Quiz.txt','w') #qF = question file
    aF = open(f'Ai Swighat\\Ans Type {i+1} of Capital Quiz.txt','w') #aF = answer file

    #Lets build a form
    qF.write('Name: \n\nRoll: \n\nDate: \n\n')
    qF.write((' '*30) + 'Quiz on American States:\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for j in range(50): #50 questions on each type
        qF.write(f'Qn.{j+1}. What is the capital of {states[j]}?\n')

        cA = capitals[states[j]] #Finding cA correct answer
        wA = list(capitals.values())
        #del wA[wA.index(cA)] # or
        wA.remove(cA)
        opt = wA + [cA]
        random.shuffle(opt)
        for k in range(4): #Each qn has 4 options
            qF.write('ABCD'[k]+f'. {opt[k]}\n')
        qF.write('\n')
        aF.write(f'{j+1}.{cA}\n')


    qF.close()
    aF.close()
