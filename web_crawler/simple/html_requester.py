
#%% Load library
from requests_html import HTMLSession
import wget

#%% Build the session
session = HTMLSession()

#%%request

URL = 'https://movie.thepan.cn/'
r = session.get(URL)
print(r)


#%%

print(r.html.links)
print(r.html.absolute_links)

# %%

site_nav = r.html.find('#site-nav',first=True)
print(site_nav.html)


# %%
site_nav2 = r.html.find('.movie-item h2', first=True)
print(site_nav2.html)
print(site_nav2.text)

# %% 
movie_titles = [movie.text for movie in r.html.find('.movie-item h2')]
print(movie_titles)
print(len(movie_titles))


# %%
release_date = [release.text for release in r.html.find('.movie-item p')]
print(release_date)

# %%
import json
output_file = 'movie.json'
movies = dict(zip(movie_titles,release_date))


with open(output_file, 'w') as output_handler:
    json.dump(movies, output_handler, indent=4)



# %%
movie_imgs = [movie.attrs['src'] for movie in r.html.find('.movie-item img')]
for url in movie_imgs:
    print(url)
    wget.download(URL+'/'+url)
#%%

