import random as rd
from math import sqrt
x1=2
x2=4

q=x2/x1
newx=x1
#geo=[x*q for y in range(9)]

geo=[x1]
for y in range(20):
	print(newx)
	geo.append(newx*q)
	newx=newx*q
B=[]
notB=[]
for y in geo:
	if sqrt(y)==int(sqrt(y)):
		B.append(int(y))
	else:
		notB.append(int(y))
print('\nq =',q,'\n', B,'\n числа є квадратами цілого числа. Всього їх',len(B),'\n\n')
for x in range(len(B)-1):
	print(B[x],B[x+1])
	x=B[x]*B[x+1]
	print (x, '= x   end')


print(notB,'- не є B. Всього їх',len(B))

