# 1. bard의 키 발급(현재는 비공식)
# 2. 시크릿 모드로 크롬 오픈
# 3. 바드 사이트로 이동
# 4. 구글 아이디로 로그인
# 5. F12  > Application -> Storage -> Cookies -> 'https://bard.google.com'의 _Secure-1PSID 에 있는 값을 키값

APIS = {
    'bard_api' : '',
    'palm_api' : '',
    'OpenAI_api' : '',
    "X_Naver_Client" : {
        'X-Naver-Client-Id' : "",
        'X-Naver-Client-Secret' : ""
        },
}