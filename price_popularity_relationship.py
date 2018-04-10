import numpy as np
import matplotlib.pyplot as plt
import json

with open("openrice_data.json") as json_file:
    original_data = json.load(json_file)

prices = []
num_reviews = []

for restaurant in original_data:
    price_range = restaurant['price-range']
    if price_range == 'Below $50':
        price = 25
    elif price_range == '$51-100':
        price = 75.5
    elif price_range == '$101-200':
        price = 150
    elif price_range == '$201-400':
        price = 300
    elif price_range == '$401-800':
        price = 600
    else:
        continue
    prices.append(price)
    num_reviews.append(int(restaurant['reviews']))

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)

#plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(prices, num_reviews)


plt.xlim(0, 700)
plt.xlabel('Price')
plt.ylim(0, 1000)
plt.ylabel('Number of reviews')

plt.show()
