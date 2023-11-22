# 파일 설명
## main.py
해당 파일에는 아래의 2가지 함수가 있습니다.
1. questions_en(question : str)
1가지의 영어 질문을 입력하면 'API.py'의 'palm_api_en(question : str)'과 'OpenAI_api(question : str)'함수를 통해서 2가지의 영어 답변을 보여줍니다.
2. questions_ko(question : str)
1가지의 한국어 질문을 입력하면 'API.py'의 'palm_api_ko(question : str)'과 'OpenAI_api(question : str)'함수를 통해서 2가지의 한국어 답변을 보여줍니다.

## API.py
해당 파일은 여러 LLM의 API를 이용하여 질문을 하면 답변을 해주는 아래의 4가지 함수가 있습니다.
1. bard_api(question : str)
질문을 하면 bard의 API를 이용해서 bard의 답변을 보여준다.
2. palm_api_en(question : str)
영어 질문을 하면 PaLM 2의 API를 이용해서 PaLM 2의 영어 답변을 보여준다.
3. palm_api_ko(question : str)
한국어 질문을 하면 'papago_translate.py'의 'translate_ko2en(question : str)'함수를 통해 한국어 질문을 영어로 바꿔서 질문을 하면 PaLM 2의 API를 이용해서 PaLM 2의 영어 답변을 'papago_translate.py'의 'translate_en2ko(answer : str)'함수를 통해 영어 답변을 한국어로 바꿔서 보여준다.
4.  OpenAI_api(question : str)
질문을 하면 OpenAI의 GPT-3(text-davinci-003)의 API를 이용해서 GPT-3의 답변을 보여준다.

## papago_translate.py
해당 파일은 네이버 개발자센터에서 발급받은 네이버 파파고의 무료 API를 이용한 아래의 2가지 함수가 있습니다.
1. translate_ko2en(question : str)
입력된 한국어를 네이버 파파고 API를 이용해 영어로 번역한다.
2. translate_en2ko(answer : str)
입력된 영어를 네이버 파파고 API를 이용해 한국어로 번역한다.

## tokens.py
'API.py'파일에서 API를 이용할떄 필요한 토큰과 키값들을 딕셔너리 형태로 저장되어 있습니다.









