import requests
from functools import partial

def search(movie):
    r = requests.get('http://www.canistream.it/services/search',
            params={'movieName': movie})
    return r.json()

def movie(movie_id, media_type):
    r = requests.get('http://www.canistream.it/services/query',
            params={'movieId': movie_id,
                    'attributes': '1',
                    'mediaType': media_type})
    return r.json()

streaming = partial(movie, media_type='streaming')
rental = partial(movie, media_type='rental')
purchase = partial(movie, media_type='purchase')
dvd = partial(movie, media_type='dvd')
xfinity = partial(movie, media_type='xfinity')
