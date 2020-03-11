# %% Load Library
import requests
import json


URL = ['https://www.instagram.com/fanshawecollege/?__a=1',
 'https://www.instagram.com/keanu.charles.reeves/?__a=1']
max_user = 0
max_user_index = 0
# %% Send out the request
for i in URL:
    r = requests.get(i)
    data = json.loads(r.text)
    current_user = data['graphql']['user']['edge_followed_by']['count']
    if(current_user>max_user):
        max_user = current_user
        max_user_index = i
    # max_user = max(max_user,current_user)
print(max_user_index)
InstgrameURL)


# %% Checkout the Results
print(r)

# %%
print(r.request.headers)
print(r.headers)

# %%
print(r.text)

# %%
print(r.status_code)

# %% 
data = json.loads(r.text)

print(data['graphql']['user']['edge_followed_by']['count'])

# %%

# %%
data = json.loads(r.text)

print(data["graphql"]['user']['edge_followed_by']['count'])


# %%

import requests

