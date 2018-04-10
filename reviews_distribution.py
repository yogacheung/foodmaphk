import matplotlib.pyplot as plt
import json

with open("openrice_data.json") as json_file:
    original_data = json.load(json_file)
    
allreviews = []

for restaurant in original_data:
    allreviews.append(int(restaurant["reviews"]))         

print(allreviews)    

plt.hist(allreviews, bins=30, histtype='stepfilled', normed=True, color='b')
plt.title("The Distribution of the number of reviews")
plt.xlabel("Reviews")
plt.ylabel("Number of restaurants")
plt.legend()

plt.show()