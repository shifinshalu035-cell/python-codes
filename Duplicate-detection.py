number =[1,1,2,2,3,3,4,4,5,5,6,6]
frequency = {}
for num in number:
    frequency[num] = frequency.get(num, 0) + 1

for n, count in frequency.items():
    if count > 1:
        print(n,"is the duplicate")
