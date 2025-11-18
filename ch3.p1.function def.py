def hello(a,b):
    print("Sorry "+ str(a)+" "+ str(b) +" times")
import random
a=["Shila","Tania","Mafia","Layla","Maria","Yun yun"]
for i in range(10):
    hello(random.choice(a),random.randint(1,1000))
    
