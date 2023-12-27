# AWS 환경에서 S3와 RDS
## user.ipynb
지정된 버킷의 경로에 있는 영상을 다운로드 받고 랜드마크 정보를 추출 후 다운로드한 영상을 삭제하고 RDS에 적재한다.  
`bucket_name` = 버킷 이름
`s3_object_key` = 영상이 있는 버킷 내의 경로
```python
import user

# 버킷 내의 경로
bucket_name = "버킷 이름"
s3_object_key = "경로와 파일 이름"

filename, json_data = user.s3_lmp(bucket_name, s3_object_key)
user.user_rds_load(filename, json_data)
```
## heatmap.ipynb
RDS에 저장되어 있는 데이터를 가지고 heatmap 그래프를 시각화함
* `table_name` = 시각화할 데이터를 조회할 테이블 이름
* `teacher` = 시각화할 강사의 이름
* `book_name` = 시각화할 책의 이름
* `lecture_num` = 시각화할 강의의 순서 예) 1, 2, 3
* `only_hand` = 아래의 `only_hand`에서 `True or False`를 선택
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