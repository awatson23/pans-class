#%% Load library
from requests_html import HTMLSession

#%% Build the session
session = HTMLSession()

#%%request
URL = 'https://www.healthline.com/'
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