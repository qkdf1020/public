# python 3.10.9에서 작성 되었습니다.

# bard
from bardapi import Bard
import os
# import bardapi

# palm
import google.generativeai as palm

# OpenAI
import openai

# 네이버 papago_api 번역
import papago_translate as pt

# api_keys
from tokens import APIS



def bard_api(question : str):
    """
    Input
        1) question (str) :
            질문
    Print
        1) bard의 답변 중에 1번쨰 답변
    Output
        1) response['content'] :
            bard의 답변 중에 1번쨰 답변
    """
    os.environ['_BARD_API_KEY'] = APIS['bard_api']
    bard = Bard()
    response = bard.get_answer(question)
    
    print("'bard'의 답변\n")
    print(response['content'])
    
    # return response['content']


def palm_api_en(question : str):
    """
    Input
        1) question (str) :
            영어 질문
    Print
        1) palm의 영어 답변
    Output
        1) response.last :
            palm의 영어 답변
    """
    palm.configure(api_key = APIS['palm_api'])
    response = palm.chat(messages = question)
    
    print("'palm'의 답변\n")
    print(response.last)
    
    # return response.last


def palm_api_ko(question : str):
    """
    Input
        1) question (str) :
            한국어 질문
    Print
        1) palm의 영어 답변을 한국어로 번역한 답변
    Output
        1) response.last :
            palm의 영어 답변을 한국어로 번역한 답변
    """
    palm.configure(api_key = APIS['palm_api'])
    
    # 한국어 질문을 영어로 번역
    response = palm.chat(messages = pt.translate_ko2en(question))
    
    print("'palm'의 답변\n")
    # 영어 답변을 한국어로 번역
    print(pt.translate_en2ko(response.last))
    
    # return pt.translate_en2ko(response.last)


def OpenAI_api(question : str):
    """
    Input
        1) question (str) :
            질문
    Print
        1) OpenAI의 답변
    Output
        1) answer :
            OpenAI의 답변
    """
    # OpenAI API 키 설정
    api_key = APIS['OpenAI_api']
    openai.api_key = api_key
    
    # OpenAI API에 요청 보내기
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150 # 최대 답변 글자수
    )
    
    # API 응답에서 답변 추출
    answer = response['choices'][0]['text'].strip()
    
    print("'OpenAI'의 답변\n")
    print(answer)
    
    # return answer
