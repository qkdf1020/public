# python 3.10.9에서 작성 되었습니다.

from model import model



print('다음 중 원하는 검색 방법을 입력하세요!!')
print('1. 숫자로 1 대 1 비교하기!!')
print('2. 이름으로 1 대 1 비교하기!!')
print('3. 이름으로 비슷한 사진 보기!!')

A = int(input('원하는 검색방법을 입력하세요 : '))

# 숫자로 비교
if A == 1 :
    num_A = int(input('1. 0 에서 808 사이의 포켓몬 번호를 입력해주세요 : '))
    if 0 > num_A :
        print('0 보다 큰 수를 입력해 주세요.')
    
    elif num_A > 809 :
        print('809 보다 작은 수를 입력해 주세요.')
        
    elif 0 <= num_A < 809 :
        num_B = int(input('2. 0 에서 808 사이의 포켓몬 번호를 입력해주세요 : '))
        if 0 > num_B :
            print('0 보다 큰 수를 입력해 주세요.')
            
        elif num_B > 809 :
            print('809 보다 작은 수를 입력해 주세요.')
        
        elif num_A == num_B :
            print('같은 번호를 입력했습니다.')
    
        elif 0 <= num_B < 809 :
            model.job_1(num_A, num_B)


# 이름으로 비교
elif A == 2 :
    name_A = str(input('1. 포켓몬 이름을 입력해주세요 : '))
    name_B = str(input('2. 포켓몬 이름을 입력해주세요 : '))
    try :
        model.job_2(name_A, name_B)
    
    except :
        raise Exception


# 이름으로 여러 이미지랑 비교
elif A == 3 :
    print('선택이 완료 되었습니다.\t잠시만 기다려주세요')
    Pokemon = str(input('포켓몬 이름을 입력해주세요 :'))
    try :
        model.job_3(Pokemon)
    
    except :
        raise Exception

else :
    print('잘못된 입력값 입니다.')