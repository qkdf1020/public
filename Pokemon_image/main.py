from model import model



print('다음 중 원하는 검색 방법을 입력하세요!!')
print('1. 숫자로 1 대 1 비교하기!!')
print('2. 이름으로 1 대 1 비교하기!!')
print('3. 이름으로 비슷한 사진 보기!!')
A = int(input('원하는 검색방법을 입력하세요 : '))
print('선택이 완료 되었습니다.\t잠시만 기다려주세요')


# 숫자로 비교
if A == 1 :
    num_A = int(input('1. 0 에서 808 사이의 포켓몬 번호를 입력해주세요 : '))
    num_B = int(input('2. 0 에서 808 사이의 포켓몬 번호를 입력해주세요 : '))
    model.twe(num_A, num_B)
    model.features_find_num(num_A, num_B)


# 이름으로 비교
elif A == 2 :
    name_A = str(input('1. 포켓몬 이름을 입력해주세요 : '))
    name_B = str(input('2. 포켓몬 이름을 입력해주세요 : '))
    num_A = model.Pokemon(name_A)
    num_B = model.Pokemon(name_B)
    model.features_find_name(num_A, num_B, name_A, name_B)