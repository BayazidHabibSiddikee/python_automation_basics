import time, threading
a = time.time()
print("Starting program at "+ str(a))
def another():
	time.sleep(3)
	print("oy   "+ str(int(time.time()-a)))
def takenap():
	time.sleep(5)
	print("Wake up  "+str(int(time.time()-a)))
	
threadobj = threading.Thread(target = takenap)
threadobj.start()
threadobj2 = threading.Thread(target=another)
threadobj2.start()


for i in range(5):
	time.sleep(1)
	print('Tick  '+str(int(time.time()-a)))
print("End of program  "+str(int(time.time()-a)))
