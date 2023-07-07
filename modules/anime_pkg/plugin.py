from jikanpy import Jikan
jikan = Jikan()

#mushishi = jikan.anime(457)
#mushishi_with_eps = jikan.anime(457, extension='episodes')

search_result = jikan.search('anime', 'mushouko tensei', page=1)

print(search_result)
#winter_2018_anime = jikan.seasons(year=2018, season='winter')

#current_season = jikan.seasons(extension='now')
