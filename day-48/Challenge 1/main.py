from selenium import webdriver
from selenium.webdriver.common.by import By


# CHALLENGE 1
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# Getting time tag
dates = driver.find_elements(By.CSS_SELECTOR, value=".medium-widget.event-widget.last time")
# Getting datetime from time tag
dates_values = [value.get_attribute("datetime").split("T")[0] for value in dates]


# Getting names
names = driver.find_elements(By.CSS_SELECTOR, value=".medium-widget.event-widget.last a")
name = [value.text for value in names]
# Slicing list
name = name[1:]


# Putting dates and names together
events = {}
position = 0

for dates_values, name in zip(dates_values, name):
    events.update({f"{position}": {"time": f"{dates_values}", "name": f"{name}"}})
    position += 1
print(events)

driver.quit()