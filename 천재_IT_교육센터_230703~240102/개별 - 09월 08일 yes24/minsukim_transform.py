# python 3.8.17에서 작성 되었습니다.

import pandas as pd



def transform_minsukim_1(_resulst) :
    
    yes_1 = pd.DataFrame(_resulst) # 입력으로 받은 (list(dict)) 형태의 데이터를 pandas DataFrame으로 변환
    yes_2 = yes_1.astype({'크롤링 날짜' : 'datetime64[ns]'}) # 'object' 형식의 크롤링 날짜를 'datetime64[ns]'으로 변경
    yes_2['yyyymm'] = yes_2['크롤링 날짜'].dt.strftime('%Y%m') # 'yyyy-mm-dd' 형식에서 'yyyymm'으로 변경 후 칼럼으로 추가
    yes_3 = yes_1[['상품번호', '상품명', '저자', '브랜드', '학제', '과목']].drop_duplicates('상품번호') # 기존 데이터에서 판매지수를 제외한 필요한 칼럼만 추출 후 중복 제거
    yes_4 = pd.DataFrame({'sales_qty_avg' : yes_2.groupby(['상품번호','yyyymm'])['판매지수'].mean()}).reset_index() # pandas DataFrame으로 변환한 데이터에서 'yyyymm' 별 판매지수 평균 구하기
    yes_5 = pd.merge(yes_4, yes_3, how = 'left', left_on = ['상품번호'], right_on = ['상품번호']) # 'yyyymm'의 판매지수 평균 데이터와 필요 칼럼 추출 데이터 합치기
    yes_6 = yes_5.rename(columns = {'상품번호' : 'code', '상품명' : 'name', '저자' : 'author', '브랜드' : 'book_group', '학제' : 'level', '과목' : 'subject'}) # 오류 방지를 위한 한글 칼럼명 영어 칼럼명으로 변경
    yes_7 = yes_6[['yyyymm', 'code', 'name', 'author', 'book_group', 'level', 'subject', 'sales_qty_avg']] # 요청한 칼럼 순서대로 순서 변경
    yyyymm = yes_2['yyyymm'].max()
    
    if len(yes_1['상품번호'].unique()) < len(yes_1['상품명'].unique()) :
        print(f"상품번호'{len(yes_1['상품번호'].unique())}'개 보다\n상품명이'{len(yes_1['상품명'].unique())}'개로 더 많아요!!!\n아마 중간에 상품명이 변경된것 같아요!!!")
        
        if len(yes_1['상품번호'].unique()) == len(yes_7['code'].unique()) :
            print(f"이번달의 상품번호는 총 '{len(yes_1['상품번호'].unique())}'개 입니다.")
            return yes_7

        elif len(yes_1['상품번호'].unique()) > len(yes_1['상품명'].unique()) :
            raise Exception(f"상품명'{len(yes_1['상품명'].unique())}'개 보다 상품번호가'{len(yes_1['상품번호'].unique())}'개로 더 많아요!!!")
    
    else : 
        raise Exception('데이터프레임이 잘못 병합된 것 같아요!!!')

def transform_minsukim_2(_resulst) :
    
    yes_1 = pd.DataFrame(_resulst) # 입력으로 받은 (list(dict)) 형태의 데이터를 pandas DataFrame으로 변환
    return yes_1

def transform_minsukim_3(_resulst) :
    
    yes_1 = pd.DataFrame(_resulst) # 입력으로 받은 (list(dict)) 형태의 데이터를 pandas DataFrame으로 변환
    yes_2 = yes_1.astype({'크롤링 날짜' : 'datetime64[ns]'}) # 'object' 형식의 크롤링 날짜를 'datetime64[ns]'으로 변경
    yes_2['yyyymm'] = yes_2['크롤링 날짜'].dt.strftime('%Y%m') # 'yyyy-mm-dd' 형식에서 'yyyymm'으로 변경 후 칼럼으로 추가
    
    return yes_2['yyyymm'].max()