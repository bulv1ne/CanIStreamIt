import requests
from functools import partial

def search(movie):
    r = requests.get('http://www.canistream.it/services/search',
            params={'movieName': movie}, 
            headers={
                'User-Agent': 
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36'
                    '(KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'})
    return r.json()

def movie(movie_id, media_type):
    r = requests.get('http://www.canistream.it/services/query',
            params={'movieId': movie_id,
                    'attributes': '1',
                    'mediaType': media_type},
            headers={
                'User-Agent': 
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36'
                    '(KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'})
    return r.json()

streaming = partial(movie, media_type='streaming')
rental = partial(movie, media_type='rental')
purchase = partial(movie, media_type='purchase')
dvd = partial(movie, media_type='dvd')
xfinity = partial(movie, media_type='xfinity')
