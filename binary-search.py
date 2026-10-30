def BinarySearch(list, key):
    low = 0
    high = len(list) - 1
    found = False

    while low <= high and not found:
        mid = (low + high) // 2

        if key == list[mid]:
            print("The item is found")
            found = True

        elif key > list[mid]:
            low = mid + 1

        else:
            high = mid - 1

    if not found:
        print("Item is not found")


list = [23, 4, 5, 6, 7, 8, 9, 90]
list.sort()

print(list)

key = int(input("Enter your number here: "))
BinarySearch(list, key)