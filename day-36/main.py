import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()


# Constants
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
STOCK = "AMD"

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_TO_SEARCH = "AMD"

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# --------------------------------------------------------------- Stock's part ----------------------------------------------------------------------------------
# # Getting API request about stock
url_stock = "https://www.alphavantage.co/query"
request_stock = requests.get(url_stock, STOCK_PARAMS)
stock_data = request_stock.json()


# # Today's date
today_date = stock_data["Meta Data"]["3. Last Refreshed"]


# # Opening of today's stock market
stock_open = float(stock_data["Time Series (Daily)"][today_date]["1. open"])


# # Yesterday's date
yesterday_date = stock_data["Time Series (Daily)"]
yesterday_date = [key for key in yesterday_date][1]


# # Closing of yesterday's stock market
stock_close = float(stock_data["Time Series (Daily)"][yesterday_date]["4. close"])


# Function for calculating drop or increase in stock
def percentage_stock():
    if stock_open > stock_close:
        percentage = round(((stock_close - stock_open) / stock_open) * 100, 2)
        percentage = f"decreased by {percentage}%"

    else:
        percentage = round(((stock_close - stock_open) / stock_close) * 100, 2)
        percentage = f"increased by {percentage}%"
    return percentage


# -------------------------------------------------- News part --------------------------------------------------------------------------------------------------
NEWS_PARAMS = {
    "apiKey": NEWS_API_KEY,
    "q": NEWS_TO_SEARCH,
    "sortBy": "popularity",
    "searchIn": "title",
    "language": "en",
    "from": yesterday_date,
    "to": today_date

}

# # Getting API request - news about our stocks
url_news = "https://newsapi.org/v2/everything"
request_news = requests.get(url_news, NEWS_PARAMS)
news_data = request_news.json()

#--------------------------------------------------------- Twilio part -----------------------------------------------------------------------------------------
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
my_phone_num = os.getenv("PHONE_NUM")

articles = news_data["articles"]

# News in here to prevent error if there are no articles
if articles:
    # # Title of the news
    title = news_data["articles"][0]["title"]

    # # Description of the news
    description = news_data["articles"][0]["description"]
    message = client.messages.create(
        body=f"{STOCK} {percentage_stock()}\n"
             f"It could be because - {title}\n"
             f"Short description - {description}",
        from_="+16167378576",
        to=my_phone_num

    )
else:
    message = client.messages.create(
        body=f"{STOCK} {percentage_stock()}\n"
             "No news found"
             "",
        from_="TWILIO_NUMBER",
        to=my_phone_num
    )

print(message.body)


