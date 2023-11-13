import requests
from tokens import APIS



def translate_ko2en(question):
    """
    Input
        1) question (str) :
            한국어 질문
    Output
        1) response.json()['message']['result']['translatedText'] :
            한국어 질문을 영어로 번역
    """
    data = {'text' : question,
            'source' : 'ko',
            'target': 'en'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = APIS['X_Naver_Client']

    response = requests.post(url, headers=header, data= data)
    rescode = response.status_code

    if(rescode==200):
        t_data = response.json()
        return response.json()['message']['result']['translatedText']
    else:
        print("Error Code:" , rescode)


def translate_en2ko(answer):
    """
    Input
        1) answer (str) :
            영어 답변
    Output
        1) response.json()['message']['result']['translatedText'] :
            영어 답변을 한국어로 번역
    """
    data = {'text' : answer,
            'source' : 'en',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = APIS['X_Naver_Client']

    response = requests.post(url, headers=header, data= data)
    rescode = response.status_code

    if(rescode==200):
        t_data = response.json()
        return response.json()['message']['result']['translatedText']
    else:
        print("Error Code:" , rescode)
