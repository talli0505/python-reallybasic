# 튜플 : 리스트랑 똑같이 생겼는데 불변형이다 리스트는 [] 튜플은 ()

a = ('사과', '감', '배')

print(a)

# 집합 : 중복을 제거해줌 // 교집합, 합집합, 차집합 다 가능

a = ['사과', '감', '배', '수박', '딸기']
b = ['배', '사과', '포도', '참외', '수박']

a_set =set(a)
b_set = set(b)

print(a_set & b_set) # 교집합
print(a_set | b_set) # 합집합

# Q. 차집합
student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
student_b = ['물리1','수학1','미술','화학2','체육']

a_set = set(student_a)
b_set = set(student_b)

print(a_set - b_set) # 차집합