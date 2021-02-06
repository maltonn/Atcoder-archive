
s=''
for i in range(3*10**5):
    s+=str(i)+' '
with open ('o.txt','w') as f:
    f.write(s)