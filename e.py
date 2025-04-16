'''import csv

with open("sample.txt",'r') as file:
    content=file.read()

print(content)
'''

s="(()()())"

l=[]
c=0

for i in s:
    if i=='(':
        c+=1
    elif i==')':
        c-=1
    if c<0:
        print("False")
        break
if c==0:
    print("True")
elif c>0:
    print("False")