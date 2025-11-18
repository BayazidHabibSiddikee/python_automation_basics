#! /usr/bin/python3
import subprocess , time
import pyautogui as pt


form='https://web.programming-hero.com/register'
name = '/home/curse/Pictures/form-name.png'
email = '/home/curse/Pictures/form-mail.png'
num = '/home/curse/Pictures/form-num.png'
pas = '/home/curse/Pictures/form-pass.png'
c_pas = '/home/curse/Pictures/form-confirm.png'
radio = '/home/curse/Pictures/radio-button.png'
ss = '/home/curse/Pictures/ss.png'

try:
	subprocess.Popen(['/usr/bin/microsoft-edge',form])
	time.sleep(4)
	
	#Fill out the form
	def fill_form(image, variable):
	#For all
		a = pt.locateOnScreen(image)
		b = pt.center(a)
		pt.click(b)
		time.sleep(1)
		pt.typewrite(variable)
		time.sleep(1)
		pt.press('enter')
		time.sleep(1)
	
	#Let's do it
	fill_form(num,'0112345645')
	fill_form(name,"Spider Man")
	fill_form(email,'sword.tyrant.error404@gmail.com')
	fill_form(pas,'qwertyuiop')
	fill_form(c_pas,'qwertyuiop')
	
	#Radio button  is little differnet just click 
	a = pt.locateOnScreen(radio)
	b = pt.center(a)
	pt.click(b)
	time.sleep(0.5)
	#Now click on 'Sign Up'
	a = pt.locateOnScreen(ss)
	b = pt.center(a)
	pt.click(b)
	time.sleep(0.5)
	
except Exception as e:
	print(str(e) + '\Done')
