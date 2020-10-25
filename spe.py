#Entering and changing input data
"""
indata=input('Введіть данні:').split(',')
iData=[]
for x in indata:
	iData.append(int(x))
tuple(iData)

print('Your data:',tuple(iData),'Sum =',sum(iData))
"""
################################
a1=[{"a":1, "b":2}, {"a":2, "b":3}, {"a":5, "b":10}, {"a":10, "b": 11}]
a2=[{"a":15, "b":12}, {"a":2, "b": 3}, {"a":17, "b": 14}, {"a":10, "b": 20} , {"a":4,  "b": 8}, {"a":12, "b": 13} ]
a3=[{"a":15, "b":  12}, {"a":2, "b": 33}] 

newa1=[]


for x in a2:
	su=((x['a']+x['b'])*2)
	newa1.append(su)
print(newa1)
SerAr=sum(newa1)/len(newa1)

print(SerAr)

