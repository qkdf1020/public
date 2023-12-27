# AWS 환경에서 S3와 RDS
## user.py
입력 받은 유저의 영상을 다운로드 받아서 상반신의 랜드마크 포인트값을 RDS에 저장한다.
## heatmap.py
RDS에 저장되어 있는 데이터를 가지고 heatmap 그래프를 시각화함
* `table_name = "테이블명"` : 시각화할 데이터를 조회할 테이블 이름
* `teacher = "강사이름"` : 시각화할 강사의 이름
* `book_name = "책이름"` : 시각화할 책의 이름
* `lecture_num = int(강의 순서)` : 시각화할 강의의 순서 예) 1, 2, 3
* `only_hand = True or False` : 아래의 `only_hand`에서 `True or False`를 선택
    * `True` : 손가락 3곳과 손목의 랜드마크 포인드의 히트맵과 어깨와 손목 사이의 거리에 대한 분산과 표준편차를 보여준다.  
    * `False` : 얼굴을 포함한 상반신의 랜드마크 포인트로 히트맵을 보여준다.
```python
import heatmap

# 조회할 테이블 이름
table_name = "테이블명"
teacher = "강사이름"
book_name = "책이름"
lecture_num = int(강의 순서)
only_hand = True or False

heatmap.rds_heatmap_720(table_name, teacher, book_name, lecture_num, only_hand)
```