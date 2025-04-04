"""
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]
l3 = []
target = 10

for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] + l2[j] == target:
            #l3.append([l1[i],l2[j]])
            l3.append([i,j])
print(l3) 
"""

string = "This is a string"

longest = '00'

for i in string.split():
    if len(i) % 2 == 0 and len(i) >= len(longest):
       longest = i

print(longest)
