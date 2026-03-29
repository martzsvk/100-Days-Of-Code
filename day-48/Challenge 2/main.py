from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Challenge 2
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# articles_n = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/main/div[3]/div[3]/div[2]/div[1]/div/div[3]/ul/li[2]/a[1]")
# articles_n.click()


# Little challenge to sign up using selenium
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Filling out first name
first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Jano")

# Filling out last name
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Veliky")

# Filling out mail
mail = driver.find_element(By.NAME, value="email")
mail.send_keys("mail.123@gmail.com")

# Clicking on the sign-up
sign_up = driver.find_element(By.XPATH, value="/html/body/form/button")
sign_up.click()

