import requests

anime_search = 'Naruto'
api_url = f'https://api.jikan.moe/v4/anime?q={anime_search}&sfw'
response = requests.get(api_url)
results = response.json()
print(results['data'][0]['title_english'])