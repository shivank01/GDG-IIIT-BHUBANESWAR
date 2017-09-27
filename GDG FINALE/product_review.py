from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import requests
import time



x=""
def printtext(root):
    global e
    string = e.get()
    global x
    x+=string 
    root.destroy()
  # print(string)   


from tkinter import *
root = Tk()

root.title('Product Review')

e = Entry(root,bg='light blue',width=70)
e.pack()
e.focus_set()

b = Button(root,text='okay',bg='purple',width=70,height=5,command=lambda:printtext(root))
b.pack(side='bottom')
root.mainloop()

#x+=" back cover"
#print(x)


driver=webdriver.PhantomJS(service_args=['--load-images=no'])
driver.get("https://www.flipkart.com/")  #specifying the website

product=driver.find_element_by_css_selector(".LM6RPg")


product.send_keys(x)

# driver.save_screenshot('testing1.png')
product.send_keys(Keys.RETURN)
driver.find_element_by_class_name("_2cLu-l").click()     
#print search.text

#time.sleep(100)
driver.save_screenshot('testing1.png')

reviews=driver.find_elements_by_class_name("qwjRop")
import sentiment_mod as s
pos=0
neg=0

for review in reviews:
	if(review.text!=''):
		#print(review.text)
		if(s.sentiment(review.text)=='pos'):
			#print("positive ")
			pos=pos+1
		else:
			#print("negative")
			neg=neg+1
			

if(pos>neg):
	rating="The product review is overall positive"
	cl='green'


elif(neg>pos):
	rating="The product review is overall negative"
	cl='red'

else:
	confidence=50.0
	rating="The product is average"
	cl='yellow'

try:
	over=rating+"\npercentage positive="+str(float(pos)/(pos+neg))+"\npercentage negative="+str(float(neg)/(pos+neg))
except:
	over="No reviews by verified users for this product"



master = Tk()
master.title('Product Review')

w = Label(master,width=50,height=50,bg=cl,  text=over)
w.pack()

mainloop()



