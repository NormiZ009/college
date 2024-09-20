li = [1,2,2,3,4,5,6,6,7,8,9,9]
li2 = []
for i in li:
    if i not in li2:
        li2.append(i)
print(li2)