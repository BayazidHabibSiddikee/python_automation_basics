#! python3
#making a stop watch to heck how much time a user takes to click 'Enter'
import time
from colorama import Fore ,Style

#display instructions
print("Press enter start stopwatch\n\
To see the time u take for every tasks,\n\
ctr+ c to stop the program")
input() #press enter to begin
print(Fore.RED+ "Started stop watch to track u"+ Style.RESET_ALL)
start = time.time()
last = start
lapnum =1
try:
	while True:
		input()
		# I will have two time one is total other is per lap time
		total = round(time.time() - start,2)
		laptime = round(time.time() - last,2)
		
		#lets print it then
		print(Fore.BLUE + f"Lap #{lapnum}: Total time: {total}, lap time: {laptime}"+Style.RESET_ALL)
		lapnum+=1
		last = time.time()
except KeyboardInterrupt:
	print(Fore.RED + '\n\nDone' + Style.RESET_ALL)
