import requests

STOCK_API_KEY = "API_KEY"
STOCK_ENDPOINTS = "https://www.alphavantage.co/query"

NEWS_API_KEY = "API_KEY"
NEWS_ENDPOINTS = "https://newsapi.org/v2/everything"

STOCK_PARAMETERS = {
    'function': "TIME_SERIES_DAILY",
    'symbol': 'TSLA',
    'apikey': STOCK_API_KEY
}

NEWS_PARAMETERS = {
    'q': 'TESLA',
    'apiKey': NEWS_API_KEY,
}


# Wrap it inside function which will return the JSON data.
# Stock api
response = requests.get(STOCK_ENDPOINTS, params=STOCK_PARAMETERS)
response.raise_for_status()
data = response.json()['Time Series (Daily)']

# News api
response_news = requests.get(NEWS_ENDPOINTS, params=NEWS_PARAMETERS)
response_news.raise_for_status()
news = response_news.json()['articles']

# Get tuple of Date and 'Close' value.
stock_data = [(date, stock['4. close']) for date, stock in data.items()]

# stock_data[8][1] closing value = 279.82 (new value), stock_data[9][1] = 261.77(old value)
stock_diff = abs(float(stock_data[0][1]) - float(stock_data[1][1]))
stock_diff_percentage = (stock_diff/float(stock_data[1][1]))*100
print(stock_diff_percentage)

# Retrieve news regarding that stock if it is moved by 5%.
if stock_diff_percentage > 1:
    three_articles = news[:3]
    formatted_message = [f'Headline: {news["title"]}. \nBrief: {news["description"]}. \nURL: {news["url"]}' for news in three_articles]
    print(formatted_message)


