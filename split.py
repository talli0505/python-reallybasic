myemail = 'abcd@sparta.co'

result = myemail.split('@')[1] # sparta.co
result2 = myemail.split('@')[1].split('.') # ['sparta', 'co']
result3= myemail.split('@')[1].split('.')[0] # sparta

print(result)
print(result2)
print(result3)

# 04.문자열 퀴즈 Q."sparta"의 앞의 3글자인 "spa"만 출력

name = 'sparta'

result = name[0:3]

print(result)

# 04.문자열 퀴즈 Q.전화번호의 지역번호 출력

phone = '02-1234-5678'

phone_num = phone.split('-')[0]

print(phone_num)