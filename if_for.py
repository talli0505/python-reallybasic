# 조건문 if

money = 3000

if money > 3400:
    print('택시를 타자!')
elif money > 1200:
    print('버스를 타자!')
else:
    print('걸어가자')

# 반복문 for

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

# enumerate : 요소의 순서를 적어줌
for i, persons in enumerate(people):
    name = persons['name']
    age = persons['age']
    print(i, name, age)
    if i > 3:
        break

# Q.리스트를 이용해 짝수만 출력
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

for num in num_list:
    if num % 2 == 0:
        print(num)

# Q.리스트를 이용해 짝수의 개수만 출력
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
count = 0
for num in num_list:
    if num % 2 == 0:
        count += 1
print(count)

# Q.리스트를 이용해 모든 숫자 더하기
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
sum = 0

for num in num_list:
    sum += num

print(sum)

# Q.리스트를 이용해 자연수 중 가장 큰 수 고르기
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
max = 0

for num in num_list:
    if max < num:
        max = num

print(max)