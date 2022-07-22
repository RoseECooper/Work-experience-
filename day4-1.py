import os
num=0
num2=0
num3=0
volist=set()
ufslist=[]
directory = 'C:/Users/Laptop/OneDrive/Documents/stfc/logfiles'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    file1 = open(f, 'r')
    Lines = file1.readlines()
#    print(Lines)

    count = 0
    for line in Lines:
        count += 1
        if count==3:
            #print("Line{}: {}".format(count, line.strip()))
            splitline1=line.split()
            #print(splitline1[8])
            vo=splitline1[8]
#!!test this out, remove the hashtags!!            
#            if vo=='snoplus.snolab.ca':
#                break
#            if vo=='cms':
#                break
            #print(vo)
            volist.add(vo)
            print(volist)
            num+=1
            #print(num)
        if count==15:
            #print("Line{}: {}".format(count, line.strip()))
            splitline2=line.split()
            #print(splitline2[8])
            userfilesize=splitline2[9]
            #print(userfilesize)
            ufslist.append(userfilesize)
            print(ufslist)
            num2=int(userfilesize)
            num3+=num2

print("total transfers: ", num)
print("total filesize: ", num3)
