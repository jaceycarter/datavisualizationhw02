#importing stuff
import json
import pprint
import matplotlib.pyplot as plt
import numpy as np

#GRAPH 2:
#bar chart looking at number of male/female within senate and governors 

govmales=0
govfemales=0
senmales=0
senfemales=0
'''
sen = []
with open('us_senators.json') as f:
        senate = f.read()
        sen += json.loads(senate)
xs = []
seny = []
for line in sen:
        xs.append(line['gender'])
        seny.append(line['number']) #don't know what my y axis would be
xs.reverse()
seny.reverse()

gov = []
with open('us_governors.json') as f:
        governor = f.read()
        gov += json.loads(governor)
govy = []
for line in gov:
        govy.append(line['number'])
xs.reverse()
govy.reverse()

'''

# with open('us_senators.json', 'r', encoding = 'ASCII') as f:
#     sen = f.read()
#     us_senators = json.loads(sen)
# with open('us_governors.json', 'r', encoding = 'ASCII') as f:
#     gov = f.read()
#     us_governors = json.loads(gov)

#  sendata=us_senators[1]
#  govdata=us_governors[1]


# sendicts = {senators['gender']: senators['']}
# sengen = sorted(sendicts.keys())
# senamount = sorted(sendicts.values())

# govdicts:
# govegen:
# govamount:

file1= 'us_senators.json'
with open(file1) as f:
    text = f.read()
    us_senators=json.loads(text)
file2= 'us_governors.json'
with open(file2) as g:
    text = g.read()
    us_governors=json.loads(text)

pprint.pprint(us_senators)

for governor in us_governors:  
    for key in governor:
        if key =='gender':
            if governor['gender']=='male':
                    govmales+=1
            if governor['gender']=='female':
                    govfemales+=1
for senator in us_senators:
    for key in us_senators['objects']:
        if key['person']['gender']=='male':
            senmales+=1            
        if key['person']['gender']=='female':
            senfemales+=1
senfemales = senfemales/2
senmales = senmales/2
print(senfemales)
print(govfemales)
print(senmales)
print(govmales)

#[0]['person']['gender']
#us_senators['objects'][1]

labels = ['Male', 'Female']
sen = [senmales, senfemales]
gov = [govmales, govfemales]

x = np.arange(len(labels)) 
width = 0.45

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, sen, width, label='Senators')
rects2 = ax.bar(x + width/2, gov, width, label='Governors')
ax.set_ylabel('Number of Elected Officials')
ax.set_title('Gender in Elected Offices')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)



