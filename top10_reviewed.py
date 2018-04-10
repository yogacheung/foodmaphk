import matplotlib.pyplot as plt
import numpy as np
import json

with open("openrice_data.json") as json_file:
    original_data = json.load(json_file)

topviews = []
topknames = []
topkviews = []

for restaurant in original_data:        
    topviews.append({"name":restaurant["name"], "reviews": int(restaurant["reviews"])})

print(topviews)    

for x in xrange(0, len(topviews)):    
    for i in xrange(x+1, len(topviews)):
        temp1 = topviews[i]        
        temp2 = topviews[x]
        if temp1["reviews"] > temp2["reviews"]:
            topviews[i], topviews[x] = topviews[x], topviews[i]

print(topviews)

for i in range (0, 10):
    views = topviews[i]    
    topknames.append(views["name"])
    topkviews.append(views["reviews"])

np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data

y_pos = np.arange(len(topknames))

ax.barh(y_pos, topkviews, align="center",
        color="green", ecolor="black")
ax.set_yticks(y_pos)
ax.set_yticklabels(topknames)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel("Reviews")
ax.set_title("Top-10 Most Reviewed Restaurants in Sha Tin")

plt.show()


