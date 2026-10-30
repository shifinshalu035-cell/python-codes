list = [10,4,0,5,100,3]
for j in range(len(list)-1):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            list[i],list[i+1] = list[i+1],list[i]

print("first iteration",list)

