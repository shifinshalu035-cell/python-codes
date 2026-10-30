number = [1,1,1,1,2,2,2,3,3,3,3,4,5,6,7,8,9,2,2,3,4,58,88,8,8]
frequency = {}
for n in number:
    frequency[n] = frequency.get(n, 0) + 1

print(number)
print(frequency)


