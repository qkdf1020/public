# 2022년 분기 별 (총 4분기) 콘텐츠 이용 실태 조사
## 기간
2023년 8월 22일 - 2023년 8월 24일

## 대상 파일
AWS의 아테나에서 내부 데이터 사용으로 파일과 출력값은 없습니다.
## 초등 3학년, 4학년, 5학년, 6학년을 대상으로 하는 콘텐츠 중 영상강의 + 문제풀이 가 함께 서비스되는 콘텐츠 중 아래의 사항을 확인할 수 있는 sql 쿼리 작성
1. 콘텐츠 별 학습을 진행한 학생 수
2. 콘텐츠 별 학습을 진행한 학생의 학년 평균
3. 콘텐츠 별 학습시간
4. 콘텐츠 별 평가문항 평균 개수, 정답문항 평균 개수, 평가점수 평균

## 참조 테이블
e_content_meta, e_member, e_test, e_media, e_study, e_learning_time_proc


## 쿼리문
```sql
SELECT med.yyyy AS "연도"
    , QUARTER(stu.enddate) AS "분기"
    , con.mcode AS "콘텐츠 코드명"
    , MAX(con.grade) AS "콘텐츠 학년"
    , ROUND(AVG(mem.grade), 2) AS "수강 학생 평균 학년"
    , COUNT(con.mcode) AS "진행한 학생 수"
    , ROUND(AVG(stu.caliper_learning_time), 2) AS "수강 학생 평균 학습 시간"
    , ROUND(AVG(tes.item_count), 2) AS "평가 문항 평균 개수"
    , ROUND(AVG(tes.correct_count), 2) AS "평가 문항 정답 평균 개수"
    , ROUND(AVG(tes.score), 2) AS "평가 점수 평균"

FROM (
    SELECT DISTINCT mcode, grade -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_content_meta"
    ) AS con -- 콘텐츠별 학년
    
INNER JOIN (
    SELECT DISTINCT userid, mcode, yyyy -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_media"
    ) AS med -- 영상 강의 콘텐츠 분기 연도
ON con.mcode = med.mcode -- 해당 칼럼 기준으로 합치기

INNER JOIN (
    SELECT DISTINCT userid, mcode, item_count, correct_count, score, yyyy -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_test"
    ) AS tes
ON med.mcode = tes.mcode
    AND med.userid = tes.userid
    AND med.yyyy = tes.yyyy -- 해당 칼럼 기준으로 합치기

INNER JOIN (
    SELECT DISTINCT userid, mcode, caliper_learning_time, enddate, yyyy -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_study"
    ) AS stu
ON med.mcode = stu.mcode
    AND med.userid = stu.userid
    AND med.yyyy = stu.yyyy -- 해당 칼럼 기준으로 합치기

INNER JOIN (
    SELECT DISTINCT userid, grade, yyyy -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_member"
    ) AS mem
ON med.userid = mem.userid
    AND med.yyyy = mem.yyyy -- 해당 칼럼 기준으로 합치기

WHERE 1 = 1
    AND con.grade BETWEEN 3 AND 6 -- 콘텐츠별 대상 학생에서 3, 4, 5, 6학년

GROUP BY con.mcode, med.yyyy, QUARTER(stu.enddate) -- 그룹화
HAVING med.yyyy = '2022' -- 원하는 연도 값 입력
    AND QUARTER(stu.enddate) = 1 -- 원하는 분기 값 입력
-- ORDER BY "진행한 학생 수" DESC
;
```



```sql
SELECT YEAR(stu.enddate) AS "연도"
    , QUARTER(stu.enddate) AS "분기"
    , con.mcode AS "콘텐츠 코드명"
    , MAX(con.grade) AS "콘텐츠 학년"
    , ROUND(AVG(mem.grade), 2) AS "수강 학생 평균 학년"
    , COUNT(con.mcode) AS "진행한 학생 수"
    , ROUND(AVG(stu.caliper_learning_time), 2) AS "수강 학생 평균 학습 시간"
    , ROUND(AVG(tes.item_count), 2) AS "평가 문항 평균 개수"
    , ROUND(AVG(tes.correct_count), 2) AS "평가 문항 정답 평균 개수"
    , ROUND(AVG(tes.score), 2) AS "평가 점수 평균"

FROM (
    SELECT DISTINCT mcode, grade -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_content_meta"
    ) AS con -- 콘텐츠별 학년
    
INNER JOIN (
    SELECT DISTINCT userid, mcode, yyyy -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_media"
    ) AS med -- 영상 강의 콘텐츠 분기 연도
ON con.mcode = med.mcode -- 해당 칼럼 기준으로 합치기

INNER JOIN (
    SELECT DISTINCT userid, mcode, item_count, correct_count, score, yyyy -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_test"
    ) AS tes
ON med.mcode = tes.mcode
    AND med.userid = tes.userid
    AND med.yyyy = tes.yyyy -- 해당 칼럼 기준으로 합치기

INNER JOIN (
    SELECT DISTINCT userid, mcode, caliper_learning_time, enddate, yyyy -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_study"
    ) AS stu
ON med.mcode = stu.mcode
    AND med.userid = stu.userid
    AND med.yyyy = stu.yyyy -- 해당 칼럼 기준으로 합치기

INNER JOIN (
    SELECT DISTINCT userid, grade, yyyy -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_member"
    ) AS mem
ON med.userid = mem.userid
    AND med.yyyy = mem.yyyy -- 해당 칼럼 기준으로 합치기

WHERE 1 = 1
    AND con.grade BETWEEN 3 AND 6 -- 콘텐츠별 대상 학생에서 3, 4, 5, 6학년

GROUP BY con.mcode, YEAR(stu.enddate), QUARTER(stu.enddate) -- 그룹화
HAVING YEAR(stu.enddate) = 2022 -- 원하는 연도 값 입력
    AND QUARTER(stu.enddate) = 1 -- 원하는 분기 값 입력
ORDER BY "진행한 학생 수" DESC
;
```



```sql
SELECT yyyy AS "연도"
    , QUARTER(stu.enddate) AS "분기"
    , mcode AS "콘텐츠 코드명"
    , MAX(con.grade) AS "콘텐츠 학년"
    , ROUND(AVG(mem.grade), 2) AS "수강 학생 평균 학년"
    , COUNT(mcode) AS "진행한 학생 수"
    , ROUND(AVG(stu.caliper_learning_time), 2) AS "수강 학생 평균 학습 시간"
    , ROUND(AVG(tes.item_count), 2) AS "평가 문항 평균 개수"
    , ROUND(AVG(tes.correct_count), 2) AS "평가 문항 정답 평균 개수"
    , ROUND(AVG(tes.score), 2) AS "평가 점수 평균"

FROM (
    SELECT DISTINCT mcode, grade -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_content_meta"
    ) AS con -- 콘텐츠별 학년
    
INNER JOIN (
    SELECT DISTINCT userid, mcode, yyyy -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_media"
    ) AS med -- 영상 강의 콘텐츠 분기 연도
USING (mcode) -- 해당 칼럼 기준으로 합치기

INNER JOIN (
    SELECT DISTINCT userid, mcode, item_count, correct_count, score, yyyy -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_test"
    ) AS tes
USING (mcode, userid, yyyy)-- 해당 칼럼 기준으로 합치기

INNER JOIN (
    SELECT DISTINCT userid, mcode, caliper_learning_time, enddate, yyyy -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_study"
    ) AS stu
USING (mcode, userid, yyyy) -- 해당 칼럼 기준으로 합치기

INNER JOIN (
    SELECT DISTINCT userid, grade, yyyy -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_member"
    ) AS mem
USING (userid, yyyy) -- 해당 칼럼 기준으로 합치기

WHERE 1 = 1
    AND con.grade BETWEEN 3 AND 6 -- 콘텐츠별 대상 학생에서 3, 4, 5, 6학년

GROUP BY mcode, yyyy, QUARTER(stu.enddate) -- 그룹화
HAVING yyyy = '2022' -- 원하는 연도 값 입력
    AND QUARTER(stu.enddate) = 1 -- 원하는 분기 값 입력
ORDER BY "진행한 학생 수" DESC
;
```



```sql
SELECT yyyy AS "연도"
    , QUARTER(stu.enddate) AS "분기"
    , mcode AS "콘텐츠 코드명"
    , MAX(con.grade) AS "콘텐츠 학년"
    , ROUND(AVG(mem.grade), 2) AS "수강 학생 평균 학년"
    , COUNT(mcode) AS "진행한 학생 수"
    , ROUND(AVG(stu.caliper_learning_time), 2) AS "수강 학생 평균 학습 시간"
    , ROUND(AVG(tes.item_count), 2) AS "평가 문항 평균 개수"
    , ROUND(AVG(tes.correct_count), 2) AS "평가 문항 정답 평균 개수"
    , ROUND(AVG(tes.score), 2) AS "평가 점수 평균"

FROM (
    SELECT DISTINCT mcode, grade -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_content_meta"
    ) AS con -- 콘텐츠별 학년
    
INNER JOIN (
    SELECT DISTINCT userid, mcode, yyyy, mm -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_media"
    ) AS med -- 영상 강의 콘텐츠 분기 연도
USING (mcode) -- 해당 칼럼 기준으로 합치기

INNER JOIN (
    SELECT DISTINCT userid, mcode, item_count, correct_count, score, yyyy, mm -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_test"
    ) AS tes
USING (mcode, userid, yyyy, mm)-- 해당 칼럼 기준으로 합치기

INNER JOIN (
    SELECT DISTINCT userid, mcode, caliper_learning_time, enddate, yyyy, mm  -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_study"
    ) AS stu
USING (mcode, userid, yyyy, mm) -- 해당 칼럼 기준으로 합치기

INNER JOIN (
    SELECT DISTINCT userid, grade, yyyy, mm -- 중복을 제거, 사용할 칼럼
    FROM "text_biz_dw"."e_member"
    ) AS mem
USING (userid, yyyy, mm) -- 해당 칼럼 기준으로 합치기

WHERE 1 = 1
    AND con.grade BETWEEN 3 AND 6 -- 콘텐츠별 대상 학생에서 3, 4, 5, 6학년

GROUP BY mcode, yyyy, QUARTER(stu.enddate) -- 그룹화
HAVING yyyy = '2022' -- 원하는 연도 값 입력
    AND QUARTER(stu.enddate) = 1 -- 원하는 분기 값 입력
ORDER BY "진행한 학생 수" DESC
;
```