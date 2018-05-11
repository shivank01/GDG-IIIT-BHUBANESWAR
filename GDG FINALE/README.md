# Review Analysis System
It is the script which automatically tells whether the product on the e-commerce websites like amazon,flipkart,etc. is good,bad or neutral on the basis of sentiments of the reviews given by their verified users.

## REQUIREMENTS
* Computer with RAM>4GB
* python3
* modules of python that should be installed
  * sklearn
  * nltk
  
## HOW TO USE?
* Make a empty container folder
* Make sure you have positive.txt and negative.txt in the same directory as of script.
* Now, We have to train the model for which we have to run picklingScript.py. It will take around 10-15 mins.
''' python3 picklingScript.py
'''
* After that we have to run product_review.py. 
''' python3 product_review.py
'''
* Wait for ~10sec. A screen will popup and you have to enter your product name(eg.-redmi note4 back cover). Keep in mind it will show you the reviews of first product in the search query of flipkart.
* After entering the product name you have wait few seconds until next screen pops up.
* popped up screen will show you your desired result.

## Noteworthy points
* The application is currently extracting only reviews of flipkart. We can extend it to any other e-commerce website by adding just few lines of code.
* As the application is in beta. Sometimes the application misbehaves and will not show you the result for some product.



