a1=[{"a":1, "b":2}, {"a":2, "b":3}, {"a":5, "b":10}, {"a":10, "b": 11}]
newa1=[]


for x in range(len(a1)):
	su=((a1[x]['a']+a1[x]['b'])*2)
	newa1.append(su)



print(newa1)