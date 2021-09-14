list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
output1=[]
output2=[]

for i in range(0,len(list1)):
    if(list1[i]>=0):
        output1.append(list1[i])
    else: continue

for i in range(0,len(list2)):
    if(list2[i]>=0):
        output2.append(list2[i])
    else: continue

print ("input1: {}".format(list1))
print ("output: {}\n".format(','.join(map(str,output1))))
print ("input2: {}\noutput: {}".format(list2,output2))