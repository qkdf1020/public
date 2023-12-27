import cv2
import json
import time
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import PoseModule_720 as pm



def video2json_720(video_path : str, save_json_file : str, points : list = list(range(66))) :
    """
    Input
        1) video_path (str) :
            동영상의 경로
        
        2) save_json_file (str) :
            json파일의 결과물이 저장될 경로
            
        3) points (list) :
            json파일로 저장할 랜드 마크 포인트를 선택
    Output
        1) 지정한 포인트을 기록한 json파일을 설정한 경로에 저장
    """
    print(f"'{video_path}' 파일 작업을 시작합니다.")
    
    start_time = time.time()  # 시작 시간
    cap = cv2.VideoCapture(video_path)
    detector = pm.poseDetector()
    list_ = []
    
    while True :
        # 영상 읽기
        success, img = cap.read()
        
        if not success:
            # 경과 시간
            current_time = time.time()
            t = int(current_time - start_time)
            print(f"경과 시간 : {t // 60}분 {t % 60}초")
            
            # 최종 결과를 JSON 파일로 저장
            with open(save_json_file, 'w', encoding='utf-8') as f:
                json.dump(list_, f, ensure_ascii = False, indent = 4)
            print(f"'{save_json_file}' 파일 저장되었습니다.\n")
            break
        
        # 각 함수 실행
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw = False)
        
        if len(lmList) != 0 :
            # new_dict = {i : lmList[i][i] for i in points}
            new_dict = {f"{key}": value for i in points for item in lmList[i:i+1] for key, value in item.items()}
            list_.append(new_dict)


def json2heatmap_720(json_path : str, save_png_file : str, points : list = list(range(33)), resolution : int = 1) :
    """
    Input 
        1) json_path (str) :
            json파일의 경로
        
        2) save_png_file (str) :
            png파일의 결과물이 저장될 경로
            
        3) points (list) :
            png파일로 저장할 랜드 마크 포인트를 선택
        
        4) resolution (int) :
            히트맵의 해상도를 1 / resolution로 저장하기 위해 선택
    Output
        1) 지정한 포인트의 히트맵 그래프 png파일을 설정한 경로에 저장
    """
    print(f"'{json_path}' 파일 작업을 시작합니다.")
    
    start_time = time.time()  # 시작 시간
    
    with open(json_path, 'r') as f:
        json_data = json.load(f)
    
    new_data = []
    n = 0
    
    while n < len(json_data) :
        result = []
        for key, value in json_data[n].items():
            temp = {key : []}
            # print(temp)
            for i in value:
                temp[key].append(int(i / resolution))
                
            result.append(temp)
            
        new_dict = {i : result[i][str(i)] for i in points}
        new_data.append(new_dict)
        n += 1
        
    # 히트맵 크기 설정
    heatmap_size = (int(720 / resolution), int(1280 / resolution))
    
    # 그래프의 크기와 DPI 설정
    plt.subplots(figsize=(int(640 / resolution), int(360 / resolution)), dpi = 4)
    
    # 히트맵 생성
    heatmap = np.zeros(heatmap_size)
    
    # 히트맵에 좌표 추가
    for frame_data in new_data :
        for key, coord_ in frame_data.items() :
            x, y = coord_
            if 0 <= x < heatmap_size[1] and 0 <= y < heatmap_size[0]:
                heatmap[y, x] += 1  # 해당 좌표의 값을 1씩 증가시킴
    
    # 히트맵 그리기 ('viriresolution', 'plasma', 'inferno', 'magma')
    sns.heatmap(heatmap, cmap = 'plasma')
    
    # 경과 시간
    current_time = time.time()
    t = int(current_time - start_time)
    print(f"경과 시간 : {t // 60}분 {t % 60}초")
    
    plt.savefig(save_png_file)
    plt.close()
    
    print(f"'{save_png_file}' 파일 저장되었습니다.\n")


def all_json2heatmap_720(h_w : list, w_h : list, new_json_data : str, save_png_file : str, points : list = list(range(33)), resolution : int = 1) :
    """
    Input
        1) h_w (list) :
            해당 강좌 폴더의 영상들의 높이와 너비
        
        2) w_h (list) :
            해당 강좌 폴더의 영상들의 너비와 높이
            
        3) json_path (str) :
            json파일의 경로
        
        4) save_png_file (str) :
            png파일의 결과물이 저장될 경로
            
        5) points (list) :
            png파일로 저장할 랜드 마크 포인트를 선택
        
        6) resolution (int) :
            히트맵의 해상도를 1 / resolution로 저장하기 위해 선택
    Output
        1) 지정한 포인트의 히트맵 그래프 png파일을 설정한 경로에 저장
    """
    start_time = time.time()  # 시작 시간
    
    new_data = []
    n = 0
    
    while n < len(new_json_data) :
        result = []
        for key, value in new_json_data[n].items():
            temp = {key : []}
            # print(temp)
            for i in value:
                temp[key].append(int(i / resolution))
                
            result.append(temp)
            
        new_dict = {i : result[points[i]][str(points[i])] for i in points}
        new_data.append(new_dict)
        n += 1
        
    # 히트맵 크기 설정
    heatmap_size = (h_w)
    
    # 그래프의 크기와 DPI 설정
    plt.subplots(figsize=(w_h), dpi = 4)
    
    # 히트맵 생성
    heatmap = np.zeros(heatmap_size)
    
    # 히트맵에 좌표 추가
    for frame_data in new_data :
        for key, coord_ in frame_data.items() :
            x, y = coord_
            if 0 <= x < heatmap_size[1] and 0 <= y < heatmap_size[0]:
                heatmap[y, x] += 1  # 해당 좌표의 값을 1씩 증가시킴
    
    # 히트맵 그리기 ('viriresolution', 'plasma', 'inferno', 'magma')
    sns.heatmap(heatmap, cmap = 'plasma')
    
    # 경과 시간
    current_time = time.time()
    t = int(current_time - start_time)
    print(f"히트맵 경과 시간 : {t // 60}분 {t % 60}초")
    
    plt.savefig(save_png_file)
    plt.close()
    
    print(f"'{save_png_file}' 파일 저장되었습니다.\n")


def calculate_distance_720(coord_1 : list, coord_2 : list) -> float :
    """
    Input
        1) coord_1 (list) :
            거리를 구할 좌표 1
            
        2) coord_2 (list) :
            거리를 구할 좌표 2
    Output
        1) distance (float) :
            입력 받은 좌표 2개의 거리 값
    """
    x1, y1 = coord_1
    x2, y2 = coord_2
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    return distance


def calculate_variance_720(distances : list) -> float :
    """
    Input
        1) distances (list) :
            분산을 구할 숫자들의 배열
    Output
        1) variance (float) :
            입력받은 숫자 배열들의 분산 값
    """
    mean = sum(distances) / len(distances)
    variance = sum((distance - mean) ** 2 for distance in distances) / len(distances)
    
    return variance


def calculate_standard_deviation_720(variance : int or float) -> float :
    """
    Input
        1) variance (int, float) :
            분산 값 (제곱근할 값)
    Output
        1) standard_deviation (float) :
            입력받은 값의 표준편차 (제곱근)
    """
    standard_deviation = variance ** 0.5
    
    return standard_deviation


def calculate_variance_standard_deviation_720(json_path : str, save_json_file : str) :
    """
    Input
        2) json_path (str) :
            json파일의 경로
        
        3) save_json_file (str) :
            json파일의 결과물이 저장될 경로
    Output
        1) 양 팔의 어깨와 손목의 거리들의 분산과 표준 편차를 json파일로 설정한 경로에 저장
    """
    print(f"'{json_path}' 파일 작업을 시작합니다.")
    
    points = [11, 12, 15, 16]

    with open(json_path, 'r') as f:
        json_data = json.load(f)

    resolutiontances_l = []
    resolutiontances_r = []
    n = 0

    while n < len(json_data) :
        result = []
        for key, value in json_data[n].items():
            temp = {key : []}
            # print(temp)
            for i in value:
                temp[key].append(i)
                
            result.append(temp)

        new_dict = {i : result[i][str(i)] for i in points}
        
        # 어꺠와 손목 사이의 거리를 하나의 리스트로 저장
        resolutiontances_l.append(calculate_resolutiontance_720(new_dict[points[0]], new_dict[points[2]]))
        resolutiontances_r.append(calculate_resolutiontance_720(new_dict[points[1]], new_dict[points[3]]))
        n += 1

    # 거리들의 분산을 계산
    variance_l = calculate_variance_720(resolutiontances_l)
    variance_r = calculate_variance_720(resolutiontances_r)

    # 거리들의 표준편차를 계산
    standard_deviation_l = calculate_standard_deviation_720(variance_l)
    standard_deviation_r = calculate_standard_deviation_720(variance_r)
    
    list_ = [{
        "왼손 분산" : variance_l,
        "오른손 분산" : variance_r,
        "왼손 표준편차" : standard_deviation_l,
        "오른손 표준편차" : standard_deviation_r
        }]
    
    # 최종 결과를 JSON 파일로 저장
    with open(save_json_file, 'w', encoding='utf-8') as f:
        json.dump(list_, f, ensure_ascii = False, indent = 4)
    
    print(list_)
    print(f"'{save_json_file}' 파일 저장되었습니다.\n")


def json2heatmap_hand_cvsd_720(video_path : str, json_path : str, save_png_file : str, save_json_file : str, resolution : int = 1) :
    """
    Input
        1) video_path (str) :
            해상도를 가져올 동영상 파일 경로
            
        2) json_path (str) :
            json파일의 경로
        
        3) save_png_file (str) :
            png파일의 결과물이 저장될 경로
        
        4) save_json_file (str) :
            json파일의 결과물이 저장될 경로
        
        4) resolution (int) :
            히트맵의 해상도를 1 / resolution로 저장하기 위해 선택
    Output
        1) 양쪽 손과 손목의 히트맵 그래프 png파일을 설정한 경로에 저장
        
        2) 양 팔의 어깨와 손목의 거리들의 분산과 표준 편차를 json파일로 설정한 경로에 저장

    """
    print(f"'{json_path}' 파일 작업을 시작합니다.")
    
    start_time = time.time()  # 시작 시간
    
    with open(json_path, 'r') as f:
        json_data = json.load(f)
    
    points_1 = list(range(15, 23))
    points_2 = [11, 12, 15, 16]
    new_data = []
    resolutiontances_l = []
    resolutiontances_r = []
    n = 0
    
    while n < len(json_data) :
        result_1 = []
        result_2 = []
        for key, value in json_data[n].items():
            temp_1 = {key : []}
            temp_2 = {key : []}
            # print(temp_1)
            # print(temp_2)
            for i in value:
                temp_1[key].append(int(i / resolution * gap))
                temp_2[key].append(i)
                
            result_1.append(temp_1)
            result_2.append(temp_2)
            
        new_dict_1 = {i : result_1[i][str(i)] for i in points_1}
        new_dict_2 = {i : result_2[i][str(i)] for i in points_2}
        new_data.append(new_dict_1)
        
        # 어꺠와 손목 사이의 거리를 하나의 리스트로 저장
        resolutiontances_l.append(calculate_resolutiontance_720(new_dict_2[points_2[0]], new_dict_2[points_2[2]]))
        resolutiontances_r.append(calculate_resolutiontance_720(new_dict_2[points_2[1]], new_dict_2[points_2[3]]))
        n += 1
    
    # 거리들의 분산을 계산
    variance_l = calculate_variance_720(resolutiontances_l)
    variance_r = calculate_variance_720(resolutiontances_r)

    # 거리들의 표준편차를 계산
    standard_deviation_l = calculate_standard_deviation_720(variance_l)
    standard_deviation_r = calculate_standard_deviation_720(variance_r)
    
    list_ = [{
        "왼손 분산" : variance_l,
        "오른손 분산" : variance_r,
        "왼손 표준편차" : standard_deviation_l,
        "오른손 표준편차" : standard_deviation_r
        }]
    
    # 히트맵 크기 설정
    heatmap_size = (video_h_w(video_path, resolution))
    
    # 그래프의 크기와 DPI 설정
    plt.subplots(figsize=(video_w_h(video_path, resolution)), dpi = 4)
    
    # 히트맵 생성
    heatmap = np.zeros(heatmap_size)
    
    # 히트맵에 좌표 추가
    for frame_data in new_data :
        for key, coord_ in frame_data.items() :
            x, y = coord_
            if 0 <= x < heatmap_size[1] and 0 <= y < heatmap_size[0]:
                heatmap[y, x] += 1  # 해당 좌표의 값을 1씩 증가시킴
    
    # 히트맵 그리기 ('viriresolution', 'plasma', 'inferno', 'magma')
    sns.heatmap(heatmap, cmap = 'plasma')
    
    # 경과 시간
    current_time = time.time()
    t = int(current_time - start_time)
    print(f"경과 시간 : {t // 60}분 {t % 60}초")
    
    plt.savefig(save_png_file)
    plt.close()
    
    print(f"'{save_png_file}' 파일 저장되었습니다.")
    
    # 최종 결과를 JSON 파일로 저장
    with open(save_json_file, 'w', encoding='utf-8') as f:
        json.dump(list_, f, ensure_ascii = False, indent = 4)
    
    print(list_)
    print(f"'{save_json_file}' 파일 저장되었습니다.\n")
