from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


# To keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initializing selenium
driver = webdriver.Chrome(chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")


# Waiting to load the site and find the element
language_button = WebDriverWait(driver, 2).until(
    ec.presence_of_element_located((By.ID, "langSelect-EN"))
)
# Clicking on language_button
language_button.click()


# While loop for 5 min
start_time = time.time()
upgrade_time = time.time()

# Finding cookie to click on
time.sleep(1)
cookie_button = WebDriverWait(driver, 5).until(
    ec.presence_of_element_located((By.ID, "bigCookie"))
)
# Cookie's count
cookie_count = driver.find_element(By.ID, value="cookies").text

# If current time (time.time) - start_time is less than 5 min (300 seconds)
while time.time() - start_time < 300:
    # Clicking on cookie
    cookie_button.click()


    # Checking if 5 sec have passed
    if time.time() - upgrade_time >= 6.5:
        # Cookie's count
        cookie_text = driver.find_element(By.ID, value="cookies").text
        cookie_count = cookie_text.split()[0].replace(",", "")
        cookie_count = int(cookie_count)

        # Upgrades
        upgrades = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

        #Buying only the most expensive upgrade
        #List of prices
        affordable_products = []

        #Finding Upgrade price
        for upgrade in upgrades:
            upgrade_text = upgrade.text
            # Getting price and also getting rid of "," between the numbers
            upgrade_price = upgrade_text.split()[1].replace(",", "")
            upgrade_price = int(upgrade_price)
            # Appending prices to list
            affordable_products.append(upgrade_price)

        # Highest valuable upgrade in list
        highest_value = len(affordable_products)
        highest_value = highest_value -1
        # Finding product on the position
        product = driver.find_element(By.ID, value=f"product{highest_value}")
        product.click()

        upgrade_time = time.time()


# Cookie per second
cookie_per_sec = WebDriverWait(driver, 5).until(
    ec.presence_of_element_located((By.ID, "cookiesPerSecond"))
)
print(f"Cookies {cookie_per_sec.text}")


