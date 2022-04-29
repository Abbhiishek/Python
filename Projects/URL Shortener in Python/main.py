import pyshorteners
import os

from dotenv import load_dotenv

load_dotenv()

long_url = input("Enter the URL to shorten: ")

# Bitly shortener service
type_bitly = pyshorteners.Shortener(api_key=os.getenv('url_shortner'))
short_url = type_bitly.bitly.short(long_url)
count = type_bitly.bitly.total_clicks(short_url)  # gives total no. of clicks.

print("The Shortened URL is: " + short_url)
print("The Total Number of Clicks is: " + str(count))
