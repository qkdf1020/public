# python 3.8.17에서 작성 되었습니다.

queries_ddb = {
    'read': {
        'book_code': '''
            {"영역":{"$eq":"기본서"}}
        ''',
        'math_book':'''
            {"영역":{"$eq":"연산"}}
        '''
    },
}