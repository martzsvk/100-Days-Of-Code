# Day 36: Stock Trading News Alert 📈

An automated financial assistant that monitors stock price fluctuations and cross-references them with the latest news headlines to explain market movements via SMS.

## What I Learned 🛠️
* **Multi-API Integration:** Coordinating data between Alpha Vantage (financial data) and NewsAPI (current events) to create a meaningful context.
* **Conditional Messaging:** Crafting different SMS templates based on whether news articles were found or not.
* **Dynamic Data Extraction:** Parsing time-series JSON data where keys (dates) change every day.

## How it Works ⚙️
1. The script gets the opening price of the current day and the closing price of the previous trading day for AMD.
2. It determines if the stock increased or decreased and by what percentage.
3. If there is a price movement, it searches for the top news articles related to that specific stock.
4. An SMS is sent via Twilio containing the price change and the headline/description of the most relevant news article.
