CanIStreamIt
============

Can I Stream It python api.

### Install

```
pip install CanIStreamIt
```

### Functions

Search for movies

```python
from canistreamit import search

search('V For Vendetta')
```

Check for watching services

```python
from canistreamit import search, streaming, rental, purchase, dvd, xfinity

search_list = search('V For Vendetta')
movie = search_list[0]

streaming(movie['_id'])
rental(movie['_id'])
purchase(movie['_id'])
dvd(movie['_id'])
xfinity(movie['_id'])

```
