birthdays={'Alice':'Apr 1','Bob':'Dec 12','Carol':'Mar 4'}
while True:
    print("Enter a name to see birthdate:")
    name=input()
    if name=='':
        break
    if name in birthdays:
        print(birthdays[name]+" is the birthday of " + name)
    else:
        print("I've no information about "+ name)
        print("Name: ")
        name=input()
        print("Birthday(month date)")
        birthdays[name]=input()
        print("Database updated:" + birthdays[name] + 'is the brithday of '+name)
            
