# python 3.10.9에서 작성 되었습니다.

import API



# 영어 질문과 답변
def questions_en(question : str):
    # API.bard_api(question)
    # print()
    API.OpenAI_api(question)
    print()
    API.palm_api_en(question)


# 한국어 질문과 답변 (네이버 papago_api를 이용해 한국어 질문을 영어로 번역 후 palm에게 보내고 palm의 영어 답변을 한국어로 다시 번역)
def questions_ko(question : str):
    # API.bard_api(question)
    # print()
    API.OpenAI_api(question)
    print()
    API.palm_api_ko(question)
