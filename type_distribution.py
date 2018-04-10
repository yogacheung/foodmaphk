import matplotlib.pyplot as plt
import json
import math

cuisine = []

with open("openrice_data.json") as json_file:
    original_data = json.load(json_file)
    
for restaurant in original_data:
   if len(cuisine) < 1:
       cuisine.append({"type": restaurant["cuisine"], "total": 1})       
       #print(cuisine)
   else:        
        check = 0
        for cuis in cuisine:
                if cuis["type"] == restaurant["cuisine"]:
                        cuis["total"] = cuis["total"] + 1
                        check = 1
                        break
        if check == 0:
             cuisine.append({"type": restaurant["cuisine"], "total": 1})     

#print(cuisine)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:

for x in xrange(0, len(cuisine)):    
    for i in xrange(x+1, len(cuisine)):
        temp1 = cuisine[i].items()
        temp2 = cuisine[x].items()
        if temp1 > temp1:
            cuisine[i], cuisine[x] = cuisine[x], cuisine[i]

sumall = 0
for cui in cuisine:
        sumall = sumall + cui["total"]

#print(sumall)
#print(cuisine)

labels = []
sizes = []
count = 4
remain = 100
for i in cuisine:
        labels.append(i["type"])
        #print(sumall/i["total"])
        ratio = int(sumall/i["total"])        
        remain = remain - ratio
        sizes.append(ratio)
        count = count - 1
        if count == 0:
                break

labels.append("other")  
sizes.append(remain)  

print(labels, sizes)

#sizes = [15, 30, 45, 10]
explode = (0, 0, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()