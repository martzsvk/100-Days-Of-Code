# Day 33: ISS Overhead Notifier 🛰️

A real-time tracking script that combines two different APIs to notify you when the International Space Station (ISS) is flying over your current location.

## What I Learned 🛠️
* **API Endpoints:** Understanding that an API is like a menu at a restaurant—you send a request to a specific URL (Endpoint) and get back data.
* **The `requests` Module:** Mastering `requests.get()` to fetch live data from the internet.
* **HTTP Response Codes:** Learning to interpret server feedback (e.g., `200` for Success, `404` for Not Found, `401` for Unauthorized).

## Requirements 📦
* Requests Library: `pip install requests`
* SMTP Library: For sending the email notification.
* Datetime: To compare local time with sunset/sunrise times.
