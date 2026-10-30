def LinerSearch(list,key):
    for i in range(len(list)):
        if key == list[i]:
            print("item is found",i)
            break
    else:
        print("item is not found")
key = int(input("enter your item here: "))
list = [2,3,4,5,6,7,8]

LinerSearch(list,key)
