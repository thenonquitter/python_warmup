#인덱스가 아닌 키에 저장
#두 개의 키값이 하나로 간주

inventory = {'knife':1, 'health kit':3, 'wood':5}

print(inventory['knife'])
inventory['knife'] = 2 #키가 존재한다면 대체
print(inventory)
inventory['gold']=7 #키가 존재하지 않는다면 추가
print(inventory)

inventory = {'knife':1, 'health kit':3, 'wood':5}

#딕셔너리 관련 함수
##inventory['gold']
print(inventory.get('gold'))
print(inventory.keys())
print(inventory.values())

#pop을 이용해 삭제. 리스트의 pop과는 다름
print(inventory.pop('knife'))
print(inventory)

#inventory.clear()
inventory['apple']=10
print(len(inventory))
print(max(inventory))
print(min(inventory))#키값이 가장 작은 것을 리턴