# 로컬에서의 분석을 위한 코드
> Local_main_720.ipynb  
* 각 랜드 마크 번호
```
얼굴
0 - nose / 코
1 - left eye (inner) / 왼쪽 눈 (안)
2 - left eye / 왼쪽 눈
3 - left eye (outer) / 왼쪽 눈 (밖)
4 - right eye (inner) / 오른쪽 눈 (안)
5 - right eye / 오른쪽 눈 
6 - right eye (outer) / 오른쪽 눈 (밖)
7 - left ear / 왼쪽 귀
8 - right ear / 오른쪽 귀
9 - mouth (left) / 입 (왼쪽)
10 - mouth (right) / 입 (오른쪽)

몸
11 - left shoulder / 왼쪽 어깨
12 - right shoulder / 오른쪽 어깨
13 - left elbow / 왼쪽 팔꿈치
14 - right elbow / 오른쪽 팔꿈치
15 - left wrist / 왼쪽 손목
16 - right wrist / 오른쪽 손목
17 - left pinky / 왼쪽 새끼손가락
18 - right pinky / 오른쪽 새끼손가락
19 - left index / 왼쪽 검지손가락
20 - right index / 오른쪽 검지손가락
21 - left thumb / 왼쪽 엄지손가락
22 - right thumb / 오른쪽 엄지손가락
23 - left hip / 왼쪽 엉덩이
24 - right hip / 오른쪽 엉덩이
25 - left knee / 왼쪽 무릎
26 - right knee / 오른쪽 무릎
27 - left ankle / 왼쪽 발목
28 - right ankle / 오른쪽 발목
29 - left heel / 왼쪽 발뒤꿈치
30 - right heel / 오른쪽 발뒤꿈치
31 - left foot index / 왼쪽 발끝
32 - right foot index / 오른쪽 발끝
```
* `lmpns = []` 추출할 랜드마크 포인트를 리스트에 넣는다.  
```python
# 랜드마크 포인트
lmpns = [list(range(23))]
points = []

for lmpn in lmpns :
    points.extend([lmpn * 2, (lmpn * 2) + 1])

print("선택된 랜드마크 :", lmpns)
```
```python
import Local_main_720 as lm

# 폴더 경로 설정
video_folder_path = "경로"
json_folder_path = "경로"

lm.video2json_folder_720(video_folder_path, json_folder_path, points)
```
* `video_folder_path = "경로"` 해당 경로 하위에 있는 영상들에 대해 작업하고 하위 폴더 내의 영상들에 대해서 작업을 합니다.

* `json_folder_path = "경로"` 영상에서 추출한 랜드마크 데이터를 json파일로 저장할 경로 지정합니다.  
지정한 경로에 `video_folder_path` 하위에 있는 파일은 해당 경로에 저장하고, 하위에 있는 강좌명으로 된 폴더를 만들고 해당 폴더에 저장합니다.