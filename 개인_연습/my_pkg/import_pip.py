# 패키지 불러오는 파일
# 파이썬 기본 패키지
import re
print("'re' import 성공!")
import os
print("'os' import 성공!")



# 실패시 install 하기
module = 'pandas' # 설치할 모듈이름 1 # 설치할 모듈이름 1
try:
    import pandas as pd # 불러올 모듈이름 # 불러올 모듈이름 1
    print(f"'{module}'을(를) import 했습니다.")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError: {e}\n'{module}'의 설치를 시작합니다.")
        !pip install {module}
        # !pip install {module} == 0.0.0 # 특정 버전으로 맞춰야 하는 경우
        try:
            # 패키지 설치에 성공하면 import
            import pandas as pd # 불러올 모듈이름 # 불러올 모듈이름 2
            print(f"'{module}'을(를) import 했습니다.")
        except ImportError:
            print(f"'{module}' 패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")
    except:
        print(f"'{module}' 패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")

module = 'numpy' # 설치할 모듈이름 1
try:
    import numpy as np # 불러올 모듈이름 1
    print(f"'{module}'을(를) import 했습니다.")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError: {e}\n'{module}'의 설치를 시작합니다.")
        !pip install {module}
        # !pip install {module} == 0.0.0 # 특정 버전으로 맞춰야 하는 경우
        try:
            # 패키지 설치에 성공하면 import
            import numpy as np # 불러올 모듈이름 2
            print(f"'{module}'을(를) import 했습니다.")
        except ImportError:
            print(f"'{module}' 패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")
    except:
        print(f"'{module}'패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")

# 시각화
module = 'matplotlib' # 설치할 모듈이름 1
try:
    import matplotlib.pyplot as plt # 불러올 모듈이름 1
    print(f"'{module}'을(를) import 했습니다.")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError: {e}\n'{module}'의 설치를 시작합니다.")
        !pip install {module}
        # !pip install {module} == 0.0.0 # 특정 버전으로 맞춰야 하는 경우
        try:
            # 패키지 설치에 성공하면 import
            import matplotlib.pyplot as plt # 불러올 모듈이름 2
            print(f"'{module}'을(를) import 했습니다.")
        except ImportError:
            print(f"'{module}' 패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")
    except:
        print(f"'{module}'패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")

module = 'seaborn' # 설치할 모듈이름 1
try:
    import seaborn as sns # 불러올 모듈이름 1
    print(f"'{module}'을(를) import 했습니다.")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError: {e}\n'{module}'의 설치를 시작합니다.")
        !pip install {module}
        # !pip install {module} == 0.0.0 # 특정 버전으로 맞춰야 하는 경우
        try:
            # 패키지 설치에 성공하면 import
            import seaborn as sns # 불러올 모듈이름 2
            print(f"'{module}'을(를) import 했습니다.")
        except ImportError:
            print(f"'{module}' 패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")
    except:
        print(f"'{module}'패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")

module = 'plotly' # 설치할 모듈이름 1
try:
    import plotly.express as px # 불러올 모듈이름 1
    print(f"'{module}'을(를) import 했습니다.")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError: {e}\n'{module}'의 설치를 시작합니다.")
        !pip install {module}
        # !pip install {module} == 0.0.0 # 특정 버전으로 맞춰야 하는 경우
        try:
            # 패키지 설치에 성공하면 import
            import plotly.express as px # 불러올 모듈이름 2
            print(f"'{module}'을(를) import 했습니다.")
        except ImportError:
            print(f"'{module}' 패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")
    except:
        print(f"'{module}'패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")

# 한글 폰트 안 깨지고 사용 가능
module = 'koreanize_matplotlib' # 설치할 모듈이름 1
try:
    import koreanize_matplotlib # 불러올 모듈이름 1
    print(f"'{module}'을(를) import 했습니다.")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError: {e}\n'{module}'의 설치를 시작합니다.")
        !pip install {module}
        # !pip install {module} == 0.0.0 # 특정 버전으로 맞춰야 하는 경우
        try:
            # 패키지 설치에 성공하면 import
            import koreanize_matplotlib # 불러올 모듈이름 2
            print(f"'{module}'을(를) import 했습니다.")
        except ImportError:
            print(f"'{module}' 패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")
    except:
        print(f"'{module}'패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")


# 기본 틀
# 'install_module_name' 1개와 import_module_name 2개만 변경 해주세요
'''
module = 'install_module_name' # 설치할 모듈이름 1
try:
    import import_module_name # 불러올 모듈이름 1
    print(f"'{module}'을(를) import 했습니다.")
except ImportError as e:
    try:
        # 패키지가 없는 경우 예외가 발생하므로 패키지를 설치
        print(f"ImportError: {e}\n'{module}'의 설치를 시작합니다.")
        !pip install {module}
        # !pip install {module} == 0.0.0 # 특정 버전으로 맞춰야 하는 경우
        try:
            # 패키지 설치에 성공하면 import
            import import_module_name # 불러올 모듈이름 2
            print(f"'{module}'을(를) import 했습니다.")
        except ImportError:
            print(f"'{module}' 패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")
    except:
        print(f"'{module}'패키지를 설치하는 동안 오류가 발생했습니다. 수동으로 설치해주세요.")
'''

'''
외부 명령 실행 도구를 사용하게 되면 보안과 안정성 문제에 노출될 수 있습니다.
더 안전한 방법은 pip 패키지 관리자를 파이썬 코드 내에서 직접 사용하는 것이 아니라,
모든 패키지 설치를 프로젝트 시작 시 또는 가상 환경 내에서 관리하는 것입니다.
이렇게 하면 필요한 패키지를 명시적으로 관리할 수 있으며,
코드 실행 중에 패키지를 동적으로 설치하려는 시도보다 더 안정적인 방법입니다.
'''