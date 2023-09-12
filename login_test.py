from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

#Set up the WebDriver
driver = webdriver.Chrome() #

#Open the web application in the browser
driver.get(r"C:\Users\ASTHA\Documents\Python Scripts\new folder\index.html")

# Find the login form elements using their 'id' attributes
username_input = driver.find_element_by_id("username")
password_input = driver.find_element_by_id("password")

# Enter your login credentials
username_input.send_keys("my_userID")
password_input.send_keys("my_passWord")

# Submit the form
password_input.send_keys(Keys.RETURN)

# Close the browser
driver.quit()
