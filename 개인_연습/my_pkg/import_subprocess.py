# 패키지 불러오는 파일
# 파이썬 기본 패키지
import re
print("'re' import 성공!")
import os
print("'os' import 성공!")
import sys
print("'sys' import 성공!")
import subprocess
print("'subprocess' import 성공!")



# 실패시 install 하기
module = 'pandas'
# desired_version = '버전번호'  # 원하는 버전을 여기에 입력
desired_version = None # 원하는 버전이 없을 경우 None으로 설정
try:
    import pandas as pd # 불러올 모듈이름 # 불러올 모듈이름 1
    print(f"'{module}' import 성공!")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError : {e}\n'{module}'의 설치를 시작합니다.")
        if desired_version is not None:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{module}=={desired_version}'])
            print(f"{module} version :", desired_version, 'install 성공!')
        else:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
            print(f"{module} :", 'install 성공!')
        try:
            # 패키지 설치에 성공하면 import
            import pandas as pd # 불러올 모듈이름 # 불러올 모듈이름 2
            print(f"'{module}' import 성공!")
        except ImportError:
            print(f"ImportError : {e}\n'오류가 발생했습니다.")
    except subprocess.CalledProcessError:
        print(f"'{module} '패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")

module = 'numpy' # 설치할 모듈이름 1
# desired_version = '버전번호'  # 원하는 버전을 여기에 입력
desired_version = None # 원하는 버전이 없을 경우 None으로 설정
try:
    import numpy as np # 불러올 모듈이름 # 불러올 모듈이름 1
    print(f"'{module}' import 성공!")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError : {e}\n{module}의 설치를 시작합니다.")
        if desired_version is not None:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{module}=={desired_version}'])
            print(f"{module} version :", desired_version, 'install 성공!')
        else:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
            print(f"{module} :", 'install 성공!')
        try:
            # 패키지 설치에 성공하면 import
            import numpy as np # 불러올 모듈이름 # 불러올 모듈이름 2
            print(f"'{module}' import 성공!")
        except ImportError:
            print(f"ImportError : {e}\n'오류가 발생했습니다.")
    except subprocess.CalledProcessError:
        print(f"'{module} '패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")

# 시각화
module = 'matplotlib' # 설치할 모듈이름 1
# desired_version = '버전번호'  # 원하는 버전을 여기에 입력
desired_version = None # 원하는 버전이 없을 경우 None으로 설정
try:
    import matplotlib.pyplot as plt # 불러올 모듈이름 # 불러올 모듈이름 1
    print(f"'{module}' import 성공!")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError : {e}\n{module}의 설치를 시작합니다.")
        if desired_version is not None:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{module}=={desired_version}'])
            print(f"{module} version :", desired_version, 'install 성공!')
        else:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
            print(f"{module} :", 'install 성공!')
        try:
            # 패키지 설치에 성공하면 import
            import matplotlib.pyplot as plt # 불러올 모듈이름 # 불러올 모듈이름 2
            print(f"'{module}' import 성공!")
        except ImportError:
            print(f"ImportError : {e}\n'오류가 발생했습니다.")
    except subprocess.CalledProcessError:
        print(f"'{module} '패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")

module = 'seaborn' # 설치할 모듈이름 1
# desired_version = '버전번호'  # 원하는 버전을 여기에 입력
desired_version = None # 원하는 버전이 없을 경우 None으로 설정
try:
    import seaborn as sns # 불러올 모듈이름 # 불러올 모듈이름 1
    print(f"'{module}' import 성공!")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError : {e}\n{module}의 설치를 시작합니다.")
        if desired_version is not None:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{module}=={desired_version}'])
            print(f"{module} version :", desired_version, 'install 성공!')
        else:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
            print(f"{module} :", 'install 성공!')
        try:
            # 패키지 설치에 성공하면 import
            import seaborn as sns # 불러올 모듈이름 # 불러올 모듈이름 2
            print(f"'{module}' import 성공!")
        except ImportError:
            print(f"ImportError : {e}\n'오류가 발생했습니다.")
    except subprocess.CalledProcessError:
        print(f"'{module} '패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")

module = 'plotly' # 설치할 모듈이름 1
# desired_version = '버전번호'  # 원하는 버전을 여기에 입력
desired_version = None # 원하는 버전이 없을 경우 None으로 설정
try:
    import plotly.express as px # 불러올 모듈이름 # 불러올 모듈이름 1
    print(f"'{module}' import 성공!")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError : {e}\n{module}의 설치를 시작합니다.")
        if desired_version is not None:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{module}=={desired_version}'])
            print(f"{module} version :", desired_version, 'install 성공!')
        else:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
            print(f"{module} :", 'install 성공!')
        try:
            # 패키지 설치에 성공하면 import
            import plotly.express as px # 불러올 모듈이름 # 불러올 모듈이름 2
            print(f"'{module}' import 성공!")
        except ImportError:
            print(f"ImportError : {e}\n'오류가 발생했습니다.")
    except subprocess.CalledProcessError:
        print(f"'{module} '패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")

# 한글 폰트 안 깨지고 사용 가능
module = 'koreanize_matplotlib' # 설치할 모듈이름 1
# desired_version = '버전번호'  # 원하는 버전을 여기에 입력
desired_version = None # 원하는 버전이 없을 경우 None으로 설정
try:
    import koreanize_matplotlib # 불러올 모듈이름 # 불러올 모듈이름 1
    print(f"'{module}' import 성공!")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError : {e}\n{module}의 설치를 시작합니다.")
        if desired_version is not None:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{module}=={desired_version}'])
            print(f"{module} version :", desired_version, 'install 성공!')
        else:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
            print(f"{module} :", 'install 성공!')
        try:
            # 패키지 설치에 성공하면 import
            import koreanize_matplotlib # 불러올 모듈이름 # 불러올 모듈이름 2
            print(f"'{module}' import 성공!")
        except ImportError:
            print(f"ImportError : {e}\n'오류가 발생했습니다.")
    except subprocess.CalledProcessError:
        print(f"'{module} '패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")

# 기본 틀
# 'install_module_name' 1개와 import_module_name 2개만 변경 해주세요
'''
module = 'install_module_name' # 불러올 모듈이름 # 불러올 모듈이름 1
# desired_version = '버전번호'  # 원하는 버전을 여기에 입력
desired_version = None # 원하는 버전이 없을 경우 None으로 설정
try:
    import import_module_name # 불러올 모듈이름 # 불러올 모듈이름 1
    print(f"'{module}' import 성공!")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError : {e}\n'{module}'의 설치를 시작합니다.")
        if desired_version is not None:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{module}=={desired_version}'])
            print(f"{module} version :", desired_version, 'install 성공!')
        else:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
            print(f"{module} :", 'install 성공!')
        try:
            # 패키지 설치에 성공하면 import
            import import_module_name # 불러올 모듈이름 # 불러올 모듈이름 2
            print(f"'{module}' import 성공!")
        except ImportError:
            print(f"ImportError : {e}\n'오류가 발생했습니다.")
    except subprocess.CalledProcessError:
        print(f"'{module} '패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")
'''