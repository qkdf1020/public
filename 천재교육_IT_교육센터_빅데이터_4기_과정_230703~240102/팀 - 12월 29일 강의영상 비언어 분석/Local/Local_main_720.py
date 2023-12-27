import os
import json
import time
import Modules_720


def video2json_folder_720(video_folder_path : str, json_folder_path : str, points : list = list(range(66))) :
    """
    Input
        1) video_folder_path (str) :
            동영상의 경로
        
        2) json_folder_path (str) :
            json파일의 결과물이 저장될 경로
            
        3) points (list) :
            json파일로 저장할 랜드 마크 포인트를 선택
    Output
        1) 지정한 포인트을 기록한 json파일을 설정한 경로에 저장
    """
    print(f"설정한 작업 경로 : {video_folder_path}")
    print(f"설정한 저장 경로 : {json_folder_path}")
    print("설정한 포인트 :", points)
    print('-' * 100)

    # 경로 내의 폴더와 파일 목록 가져오기
    for dirpath, dirnames, filename in os.walk(video_folder_path) :
        for dirname in dirnames:
            new_video_folder_path = os.path.join(json_folder_path, dirname)
            
            try:
                # 디렉토리를 만듭니다.
                os.makedirs(new_video_folder_path)
                print(f"'{new_video_folder_path}' 디렉토리를 생성합니다.")
                
            except FileExistsError:
                print(f"'{new_video_folder_path}' 디렉토리는 이미 존재합니다.")
                pass
        
        print('-' * 100)
        
        # 현재 작업하고 있는 폴더이자 저장될 폴더 이름
        save_folder = os.path.split(dirpath)[-1]
        print(f"'{save_folder}' 폴더의 작업을 시작합니다.")
        
        if len(filename) == 0 :
            print(f"'{save_folder}' 폴더에는 파일이 없습니다.")
        
        # 설정한 저장 경로에 현재 작업중인 폴더 이름 결합
        new_file_path = os.path.join(json_folder_path, save_folder)
                
        for file in filename :            
            if file.endswith(".mp4") :
                # 작업할 'mp4'파일의 경로
                video_path = os.path.join(dirpath, file)
                
                # 파일 이름과 확장자 분리
                filename_, extension = os.path.splitext(file)
                
                # 저장될 파일 확장자명 변경
                output_filename = f"{filename_}.json"
                
                # 최종적으로 저장될 경로와 파일명 결합
                save_json_file = os.path.join(new_file_path, output_filename)
                
                # 작업할 모듈 실행
                Modules_720.video2json_720(video_path, save_json_file, points)


def json2heatmap_folder_720(video_folder_path : str, json_folder_path : str, png_folder_path : str, points : list = list(range(33)), resolution : int = 1) :
    """
    Input
        1) video_folder_path (str) :
            해상도를 불러올 동영상의 경로
        
        2) json_folder_path (str) :
            json파일의 경로
            
        3) png_folder_path (str) :
            히트맵png파일이 저장될 경로
            
        4) points (list) :
            json파일에서 읽어서 히트맵으로 저장할 랜드 마크 포인트를 선택
        
        5) resolution (int) :
            히트맵의 해상도결정 '1/resolution'
    Output
        1) 지정한 포인트을 기록한 히트맵png파일을 설정한 경로에 저장
    """
    print(f"해상도 가져올 경로 : {video_folder_path}")
    print(f"설정한 작업 경로 : {json_folder_path}")
    print(f"설정한 저장 경로 : {png_folder_path}")
    print(f"설정한 포인트 : {points}")
    print(f"설정한 원본대비 png 해상도 : 1/{resolution}")
    print('-' * 100)

    # 경로 내의 폴더와 파일 목록 가져오기
    for dirpath, dirnames, filename in os.walk(json_folder_path) :
        for dirname in dirnames:
            new_png_folder_path = os.path.join(png_folder_path, dirname)
            
            try:
                # 디렉토리를 만듭니다.
                os.makedirs(new_png_folder_path)
                print(f"'{new_png_folder_path}' 디렉토리를 생성합니다.")
            except FileExistsError:
                print(f"'{new_png_folder_path}' 디렉토리는 이미 존재합니다.")
                pass
        
        print('-' * 100)
        
        # 현재 작업하고 있는 폴더이자 저장될 폴더 이름
        save_folder = os.path.split(dirpath)[-1]
        print(f"'{save_folder}' 폴더의 작업을 시작합니다.")
        
        if len(filename) == 0 :
            print(f"'{save_folder}' 폴더에는 파일이 없습니다.")
        
        # 설정한 저장 경로에 현재 작업중인 폴더 이름 결합
        new_file_path = os.path.join(png_folder_path, save_folder)
                
        for file in filename :
            if file.endswith(".json") :
                # 작업할 'json'파일의 경로
                json_path = os.path.join(dirpath, file)
                
                # 파일 이름과 확장자 분리
                filename_, extension = os.path.splitext(file)
                
                # 저장될 파일 확장자명 변경
                output_filename = f"{filename_}.png"
                
                # 최종적으로 저장될 경로와 파일명 결합
                save_png_file = os.path.join(new_file_path, output_filename)
                

                
                # 작업할 모듈 실행
                Modules_720.json2heatmap_720(json_path, save_png_file, points, resolution)
    

def all_json2heatmap_folder_720(video_folder_path : str, json_folder_path : str, png_folder_path : str, points : list = list(range(33)), resolution : int = 1) :
    """
    Input
        1) video_folder_path (str) :
            해상도를 불러올 동영상의 경로
        
        2) json_folder_path (str) :
            json파일의 경로
            
        3) png_folder_path (str) :
            히트맵png파일이 저장될 경로
            
        4) points (list) :
            json파일에서 읽어서 히트맵으로 저장할 랜드 마크 포인트를 선택
        
        5) resolution (int) :
            히트맵의 해상도결정 '1/resolution'
    Output
        1) 지정한 포인트을 기록한 히트맵png파일을 설정한 경로에 저장
    """
    print(f"해상도 가져올 경로 : {video_folder_path}")
    print(f"설정한 작업 경로 : {json_folder_path}")
    print(f"설정한 저장 경로 : {png_folder_path}")
    print(f"설정한 원본대비 png 해상도 : 1/{resolution}")
    print(f"설정한 포인트 : {points}")
    print('-' * 100)

    try:
        # 디렉토리를 만듭니다.
        os.makedirs(png_folder_path)
        print(f"'{png_folder_path}' 디렉토리를 생성합니다.")
    except FileExistsError:
        print(f"'{png_folder_path}' 디렉토리는 이미 존재합니다.")
        pass

    # 경로 내의 폴더와 파일 목록 가져오기
    for dirpath, dirnames, filename in os.walk(video_folder_path) :
        print('-' * 100)
        
        # 현재 작업하고 있는 폴더이자 저장될 폴더 이름
        save_folder = os.path.split(dirpath)[-1]
        
        h_w_list = []
        
        for file in filename :
            if file.endswith(".mp4") :
                # # 해상도를 가져오기 위한 작업
                h_w_path = os.path.join(video_folder_path, save_folder)
                video_path = os.path.join(h_w_path, file)
                h_w = Modules_720.video_h_w(video_path)
                h_w_list.append(h_w)
                
        if not h_w_list:
            print(f"'{save_folder}' 폴더에 영상 파일이 없습니다.\n")
        
        elif max(h_w_list) != min(h_w_list) :
            print(f"'{save_folder}' 폴더의 영상들의 해상도가 일치하지 않아서 작업을 진행 할 수 없습니다.\n")

        else :
            # 히트맵에 적용될 해상도
            w_h_list = [(h, w) for w, h in h_w_list]
            h_w = h_w_list[0]
            w_h = w_h_list[0]
            
            print(f"'{save_folder}' 폴더의 영상들의 해상도가 {w_h}로 일치하여 작업을 시작합니다.\n")
            
            start_time = time.time()  # 시작 시간
            
            new_json_data = []
            
            for file in filename :
                if file.endswith(".mp4") :
                    # 파일 이름과 확장자 분리
                    filename_, extension = os.path.splitext(file)
                    
                    # 파일 확장자명 변경
                    json_filename = f"{filename_}.json"
                    
                    # 작업할 'json'파일의 경로
                    json_file_path_1 = os.path.join(save_folder, json_filename)
                    json_file_path_2 = os.path.join(json_folder_path, json_file_path_1)
                    
                    # 저장될 파일 확장자명 변경
                    output_filename = f"{save_folder}.png"
                    
                    # 최종적으로 저장될 경로와 파일명 결합
                    save_png_file = os.path.join(png_folder_path, output_filename)
                    
                    # json파일 결합                
                    with open(json_file_path_2, 'r', encoding = 'utf-8') as json_file :
                        json_data = json.load(json_file)
                        new_json_data.extend(json_data)
                        
            # 경과 시간
            current_time = time.time()
            t = int(current_time - start_time)
            print(f"'json'파일 결합 경과 시간 : {t // 60}분 {t % 60}초")
                    
            # 작업할 모듈 실행
            Modules_720.all_json2heatmap(h_w, w_h, new_json_data, save_png_file, points, resolution)


def json2heatmap_hand_folder_720(video_folder_path : str, json_folder_path : str, png_folder_path : str, resolution : int = 1) :
    """
    Input
        1) video_folder_path (str) :
            해상도를 불러올 동영상의 경로
        
        2) json_folder_path (str) :
            json파일의 경로
            
        3) png_folder_path (str) :
            히트맵png파일이 저장될 경로
        
        4) resolution (int) :
            히트맵의 해상도결정 '1/resolution'
    Output
        1) 지정한 포인트을 기록한 히트맵png파일을 설정한 경로에 저장
    """
    print(f"해상도 가져올 경로 : {video_folder_path}")
    print(f"설정한 작업 경로 : {json_folder_path}")
    print(f"설정한 저장 경로 : {png_folder_path}")
    print(f"설정한 원본대비 png 해상도 : 1/{resolution}")
    print('-' * 100)

    # 경로 내의 폴더와 파일 목록 가져오기
    for dirpath, dirnames, filename in os.walk(json_folder_path) :
        for dirname in dirnames:
            new_png_folder_path = os.path.join(png_folder_path, dirname)
            
            try:
                # 디렉토리를 만듭니다.
                os.makedirs(new_png_folder_path)
                print(f"'{new_png_folder_path}' 디렉토리를 생성합니다.")
            except FileExistsError:
                print(f"'{new_png_folder_path}' 디렉토리는 이미 존재합니다.")
                pass
        
        print('-' * 100)
        
        # 현재 작업하고 있는 폴더이자 저장될 폴더 이름
        save_folder = os.path.split(dirpath)[-1]
        print(f"'{save_folder}' 폴더의 작업을 시작합니다.")
        
        if len(filename) == 0 :
            print(f"'{save_folder}' 폴더에는 파일이 없습니다.")
        
        # 설정한 저장 경로에 현재 작업중인 폴더 이름 결합
        new_file_path = os.path.join(png_folder_path, save_folder)
                
        for file in filename :
            if file.endswith(".json") :
                # 작업할 'json'파일의 경로
                json_path = os.path.join(dirpath, file)
                
                # 파일 이름과 확장자 분리
                filename_, extension = os.path.splitext(file)
                
                # 저장될 파일 확장자명 변경
                output_filename_1 = f"{filename_}.png"
                output_filename_2 = f"{filename_}.json"
                
                # 최종적으로 저장될 경로와 파일명 결합
                save_png_file = os.path.join(new_file_path, output_filename_1)
                save_json_file = os.path.join(new_file_path, output_filename_2)
                
                # 해상도를 가져오기 위한 작업
                h_w_path = os.path.join(video_folder_path, save_folder)
                video_filename = f"{filename_}.mp4"
                video_path = os.path.join(h_w_path, video_filename)
                
                # 작업할 모듈 실행
                Modules_720.json2heatmap_hand_cvsd(video_path, json_path, save_png_file, save_json_file, resolution)
