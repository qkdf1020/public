# 사용할 패키지를 import
try:
    import pandas as pd
    print(f"version : {pd.__version__}, 'pandas' install 성공!")
except ImportError as e:
    print(e)

try:
    import numpy as np
    print(f"version : {np.__version__}, 'numpy' install 성공!")
except ImportError as e:
    print(e)