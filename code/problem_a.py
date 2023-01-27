import requests
def popular_count():

    # 여기에 코드를 작성합니다.  
    # https://developers.themoviedb.org/3/movies/get-popular-movies
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key':'b3628728851d758a9fb78c3d38b86613',
        'language':'ko',
        'region':'KR'
    }

    reponse = requests.get(BASE_URL+path, params=params).json()
    rlt= reponse['results']
    lst=[]
    for i in range(len(rlt)):
        s=rlt[i]
        stitle=s['title']
        lst.append(stitle)
    
    title_count=len(lst)
    return title_count

print(popular_count())

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
