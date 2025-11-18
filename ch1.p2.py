name = ''
while name !="Your name":
    print("Enter name: ")
    name = input()
    print("Hello " + name)
    if name != "Your name":
        print("Enter real name")
    else:
        break
print("Thank u")
