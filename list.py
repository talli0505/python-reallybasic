# 리스트는 순서가 중요하게 값을 담음(key, value), append는 추가, [:]이용해서 자를수 있음, sort 이용한 정렬, 값 in 리스트 해서 있으면 참 없으면 거짓 가능

a_list = [1,5,6,3,2]

a_list.sort(reverse=True) # 6,5,4,3,2,1

result = (99 in a_list)

print(a_list)
print(result)