import random


disposableemaill = open("domains.txt","r+")
temp = disposableemaill.readlines()
domain = []
domain += temp
for i in temp:
    if(i[0].isnumeric()):
        domain.remove(i)


username = []
with open("/home/sila/work/security/wordlists/rockyou.txt") as myfile:
    temp = [next(myfile) for x in range(4*129017)]
for i in temp:
    if(i[0].isnumeric()==False):
        username.append(i)


for i in range(len(username)):
    username[i] = username[i][0:-2]
    

emailid = []
for i in domain:
    for x in range(2):
        y = random.choice(username)
        emailid.append(y+"@"+i)


writes = open("disposable-email-ids.txt","w+")
writes.writelines((emailid))

