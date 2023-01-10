# 함수

def bus_rate(age):
    if age > 65:
        print('무료입니다')
        return 0
    elif age > 20:
        print('성인입니다')
        return 1200
    else:
        print('청소년입니다')
        return 750

myrate = bus_rate(15)
print(myrate)

def check_gender(pin):
    num = pin.split('-')[1][:1]
    if int(num) % 2 == 0:
        print('여성')
    else :
        print('남성')

check_gender('200101-1012345')
check_gender('200101-2012345')
check_gender('200101-3012345')

# # 함수 심화, 함수 매개변수

# def cal(a,b=2):
#     return a+2*b
#
# result = cal(1,3)
# print(result)