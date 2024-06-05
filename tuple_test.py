#tuple warm-up

item = ("health kit", 4, 55, True)
name = item[0]
quantity = item[1]
print(name)
#item[1] = 10
item = ("knife", 1) #아예 다른 정보를 저장
print(item)
print(item.count('knife'))
print(item.index(1)) #어떤 항목의 첫번째를 리턴 

item = (0, 1, 2)
print(min(item))
print(max(item))
print(len(item))