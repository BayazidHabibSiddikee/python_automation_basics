import random
def get(a):
    if a==1:
        return "Fuck you"
    elif a == 2:
        return "Sorry"
    elif a == 3:
        return "ohh shit"
    else:
        return "Doubtful"
for i in range(5):
    fortune = get(random.randint(1,4))
    print("She's gonna say: " + fortune)
