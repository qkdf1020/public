import os
print("'os' import 성공!")
import pandas as pd
print(f"'pandas' install 성공! version : {pd.__version__}")



def cur_dir_1() -> None:
    """
    Input
        1) None
    Print
        1) 현재 작업 디렉토리
        2) 현재 디렉토리 내의 파일과 하위 디렉토리 목록 리스트
    Output
        1) dir_list (list) :
            현재 디렉토리 내의 파일과 하위 디렉토리 목록 리스트
    """
    # 현재 작업 디렉토리 확인
    cur_directory = os.getcwd()
    print('\n현재 작업 디렉토리 :\n', cur_directory)
    
    # 현재 디렉토리 내의 파일과 하위 디렉토리 목록 -> 리스트로 반환
    dir_list = os.listdir(cur_directory)
    print('\n현재 디렉토리 내의 파일과 하위 디렉토리 목록 :\n', dir_list)
    
    return dir_list


def cur_dir_2(directory_name : str):
    """
    Input
        1) directory_name (str) :
            현재 작업 디렉토리에서 확인하고 싶은 디렉토리 이름
    Print
        1) directory_name (str) 내의 파일과 하위 디렉토리 목록 리스트
    """
    # 현재 디렉토리에서 특정 디렉토리 내의 파일과 하위 디렉토리 목록 -> 리스트로 반환
    dir_listdir = os.path.join(os.getcwd(), directory_name)
    data_list = os.listdir(dir_listdir)
    print(f'\n{dir_listdir} 내의 파일과 하위 디렉토리 목록 :\n', data_list)
    
    return data_list


def dir_csv_excel(directory_name : str, index_col : int or str = None, encoding : str = None):
    """
    Input
        1) directory_name (str) :
            현재 작업 디렉토리에서 cvs, excel 파일들을 불러올 디렉토리 이름
        2) index_col (int | str) = None :
            인덱스로 사용할 열의 번호 또는 이름을 지정
        3) encoding (str) = None :
            파일의 인코딩을 지정
            한글 파일 에러 : 'cp949'
            아스키 코드 에러 : 'ISO-8859-1'
    Output
        1) dataset (dict) :
            directory_name (str) 내의 csv, excel 파일,
            변수 = dir_csv_excel('directory_name')['파일이름.확장자']로 사용
    """
    # 현재 디렉토리에서 특정 디렉토리 내의 파일과 하위 디렉토리 목록 -> 리스트로 반환
    dir_listdir = os.path.join(os.getcwd(), directory_name)
    data_list = os.listdir(dir_listdir)
    print(f"\n'{dir_listdir}' 내의 파일과 하위 디렉토리 목록 :\n", data_list)

    # csv 파일 대량 불러오기 -> dict 형태로 반환
    dataset = dict()
    
    try:
        for data in data_list:
            if data.lower().endswith('.csv'): # csv 파일만
                print(data) # csv 파일들 출력
                dataset[data] = pd.read_csv(os.path.join(dir_listdir, data), index_col = index_col, encoding = encoding)
            
            elif data.lower().endswith('.xls') or data.lower().endswith('.xlsx'):
                print('/n', data) # excel 파일들 출력
                dataset[data] = pd.read_excel(os.path.join(dir_listdir, data), index_col = index_col)
    
    except Exception as e:
        print(e)
        
    return dataset

def check_df(df):
    """
    Input
        1) df (DataFrame) :
            확인하고 싶은 데이터 프레임
    Print
        1) df (DataFrame)의 rows x columns
    display
        1) df (DataFrame)의 칼럼별(column)
        유니크의 개수(unique_cut), 비결측치의 개수(non_null_cut), 데이터 타입(dtype),
        결측치의 개수(null_cut), 결측치의 비율(null_ratio)
        2) df (DataFrame)의 칼럼중, 데이터 타입이 수치형인 칼럼들의 describe()
        데이터의 총 개수, 평균, 표준 편차, 최솟값, 25, 50, 75 백분위수, 최댓값
    """
    print('rows x columns :', df.shape) # (행 개수, 열 개수)
    # 칼럼별 unique 개수 확인
    columns_info = dict()
    columns = df.columns
    for col in columns:
        columns_info[col] = len(df[col].unique())
    data = [{'index': col, 'unique_cut': count} for col, count in columns_info.items()]
    unique_cut_df = pd.DataFrame(data)
    # unique_cut_df.set_index('index').T
    non_null_cut_df = pd.DataFrame(df.count()).rename(columns = {0 : 'non_null_cut'}).reset_index()# 칼럼별 비결측치 개수
    info_df = pd.DataFrame(df.dtypes).rename(columns = {0 : 'dtype'}).reset_index() # 데이터 프레임 info
    # 칼럼별 결측지 비율 확인
    null_cnt_df = pd.DataFrame(df.isnull().sum()).rename(columns = {0 : 'null_cut'}).reset_index()
    null_cnt_df['null_ratio'] = round(null_cnt_df['null_cut'] / len(df) * 100, 2)
    # 합치기
    unique_non_null_cut_df = pd.merge(unique_cut_df, non_null_cut_df)
    unique_non_null_info_cut_df = pd.merge(unique_non_null_cut_df, info_df)
    unique_non_null_info_null_cut_df = pd.merge(unique_non_null_info_cut_df, null_cnt_df).rename(columns = {'index' : 'column'})
    # describe - 통계
    int_float_cnt  = unique_non_null_info_null_cut_df[(unique_non_null_info_null_cut_df['dtype'] == 'int64') |
                     (unique_non_null_info_null_cut_df['dtype'] == 'float64')]
    # 보여주기
    if len(unique_non_null_info_null_cut_df.columns) >= len(int_float_cnt.columns):
        len_number = len(unique_non_null_info_null_cut_df.columns)
    else:
        len_number = len(int_float_cnt.columns)
    pd.set_option('display.max_columns', len_number)            
    display(unique_non_null_info_null_cut_df)
    display(df.describe())

