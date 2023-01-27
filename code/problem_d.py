import requests
from pprint import pprint


def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key':'b3628728851d758a9fb78c3d38b86613',
        'query':title,
        'language':'ko',
        'region':'KR'
    }
    reponse = requests.get(BASE_URL+path, params=params).json()
    rlt = reponse['results']
    if rlt == []:
        return None    
    

    first_movie = rlt[0]['id']
    # print(first_movie)

    url = f'https://api.themoviedb.org/3/movie/{first_movie}/recommendations?api_key=b3628728851d758a9fb78c3d38b86613&language=ko&page=1'
    reponse = requests.get( url).json()
    rlt2=reponse['results']
    lst=[]
    for i in rlt2:
        stitle=i['title']
        lst.append(stitle)
    return lst
""" 
    BASE_URL_2 = 'https://api.themoviedb.org/3'
    path_2 = '/movie/{first_movie}/recommendations'
    params_2 = {
        'api_key':'b3628728851d758a9fb78c3d38b86613'
        'language':'ko',
        'page':1
    }
    reponse2 = requests.get(BASE_URL_2+path_2, params=params_2).json()
    print(reponse2) """

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
