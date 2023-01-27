import requests
from pprint import pprint


def credits(title):
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

    first_movie = rlt[0]['id']
    # 여기에 코드를 작성합니다.  
    if rlt == []:
        return None    
    
    url = f'https://api.themoviedb.org/3/movie/{first_movie}/credits?api_key=b3628728851d758a9fb78c3d38b86613&language=ko'
    reponse = requests.get(url).json()
    rlt2=reponse['cast']
    print(rlt2)
    cast_lst=[]
    for i in rlt2:
        if i['cast_id']<10:
            cast_lst.append(i['name'])
    print(cast_lst)

    rlt3=reponse['crew']
    print(rlt3)
    crew_lst=[]
    for i in rlt3:
        if i['department']=='Directing':
            crew_lst.append(i['name'])
    print(crew_lst)

    dic={}
    dic['cast']=cast_lst
    dic['directing']=crew_lst
    return dic


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    # pprint(credits('검색할 수 없는 영화'))
    # None
