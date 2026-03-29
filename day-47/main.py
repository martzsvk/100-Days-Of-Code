from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# Constants
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# Request to site
response = requests.get(url=url, headers={"Accept-Language": "en-US",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0"})

soup = BeautifulSoup(response.text, "html.parser")
# Scraping whole price of product
whole_price = soup.find(class_="a-price-whole")
whole_price = whole_price.get_text()

# Scraping decimal price of product
decimal_price = soup.find(class_="a-price-fraction")
decimal_price = decimal_price.get_text()

# Full price
price = float(whole_price + decimal_price)


# Sending an email
if price < 80:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Discount \n\n Look here {url}")
