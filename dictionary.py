a_dict = {'name':'bob', 'age':27, 'friend':['영희','철수']}

a_dict['height'] = 180 # 추가

result = ('height' in a_dict) # 참 거짓 여부
print(a_dict['friend'][1])
print(a_dict)
print(result)

people = [
    {'name':'bob', 'age':27},
    {'name':'john', 'age':30}
]

print(people[1]['age'])

# Q. smith의 science 점수를 출력

people = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]

result = people[2]['score']['science']

print(result)