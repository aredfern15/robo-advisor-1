# this is the "app/robo_advisor.py" file
#had help from Professor Rossetti's screencast, Nolan Matsko, and Annabelle Zebrowski 

#imports needed for robo advisor
import csv
import json
import os
import requests
from dotenv import load_dotenv 

load_dotenv()

#Date and Time from https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import datetime  

#using now() to get current time  
now = datetime.now()
#print("now =", now)

dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
#for price formatting throughout the entire thing

#price for USD
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


#INFO INPUTS
#worked with Nolan Matsko and Annabelle Zebrowski 
#checking if ticker has a valid number of characters
ticker = input("Please enter the stock ticker that you would like to evaluate: ")

if len(ticker) >1 or len(ticker) <= 5: 
    pass
else: 
    print("Oops, you have entered an invalid stock ticker. Please try again with a symbol such as 'IBM'.")
    exit()

#check if ticker has a number
#helped by olisteadman on https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number


for tickers in ticker: 
    if tickers.isdigit(): 
        ticker_digits = True

if ticker_digits == False: 
    pass
else:
    print("Oops, you have entered an invalid stock ticker with a digit. Please try again with a symbol such as 'IBM'.")
    exit()


symbol = ticker
api_key = os.environ.get("ALPHAVANTAGE_API_KEY") 
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
#print("URL:", request_url)

response = requests.get(request_url)
parsed_response = json.loads(response.text)


#check if ticker exists
#help about checking if a key is in a JSON array 
#help came from Robert LUgo on https://stackoverflow.com/questions/24898797/check-if-key-exists-and-iterate-the-json-array-using-python

try:
    last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
except:
    print("Oops, the stock you entered does not exist. Please try again with a symbol such as 'IBM'.")
    exit()


#last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys())

latest_day = dates[0]

latest_close =  float(tsd[latest_day]["4. close"])#> 1,000,000

high_prices =[]
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

#INFO OUTPUTS

#csv_file_path = "data/prices.csv" # a relative filepath
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"], 
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]    
        })


#rec_choice 
a = latest_close
b = recent_low

if a <= (1.15 * b):
    rec_choice = "Buy!"
    rec_reason = "Buy! The stock's latest closing price is less than or equal to 15 percent above its recent low."

else: 
    rec_choice = "Don't buy!"
    rec_reason = "Don't buy! The stock's latest closing price is more than 15 percent above its recent low."



print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA")
print(f"REQUEST AT: {dt_string}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print(f"RECOMMENDATION: {rec_choice}")  
print(f"RECOMMENDATION REASON: {rec_reason}") 
print("-------------------------") 
print(f"WRITING DATA TO CSV... {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


