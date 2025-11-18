#! python3
msg = ' The ADJECTIVE panda walked to the NOUN and then VERB .A nearby NOUN was unaffected by these events. '
ml = msg.split()
#print(ml)
for i in range(len(ml)):
    if ml[i].upper()=='ADJECTIVE' or  ml[i].upper()=='NOUN' or  ml[i].upper()=='VERB':
        ml[i]=input("Enter an "+ml[i].lower()+':\n')
        
print(' '.join(ml))
