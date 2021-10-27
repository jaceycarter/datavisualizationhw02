#importing stuff
import json
import pprint
import matplotlib.pyplot as plt
import numpy as np


#with open('us_senators.json', 'r', encoding = 'ASCII') as f:
        #sen = f.read()
        #us_senators = json.loads(sen)
#with open('us_governors.json', 'r', encoding = 'ASCII') as f:
        #gov = f.read()
        #us_governors = json.loads(gov)

#GRAPH 1
democrat=0
republican=0
independent=0

file= 'us_senators.json'
with open(file) as f:
    text = f.read()
    us_senators=json.loads(text)
pprint.pprint(us_senators)

for senators in us_senators['objects']:
    for key in senators:
        if key =='party':
            if senators['party']=='Republican':
                republican+=1
            if senators['party']=='Democrat':
                democrat+=1
            if senators['party']=='Independent':
                independent+=1

print(republican)
print(democrat)
print(independent)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Republicans', 'Democrats', 'Independent'
sizes = [50, 48, 2]
explode = (0, 0.1, 0)  
colors = ["red", "blue", "purple"]


fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors,
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.legend(title = "Party:")
plt.title("US Senators and Party Affiliation")
plt.show()
