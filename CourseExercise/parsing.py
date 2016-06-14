import re
import string
y=re.findall('[0-9]+',open('text1.txt','r').read())
sum=0
for i in range(0,len(y)):
    sum=sum+int(y[i])

print sum
