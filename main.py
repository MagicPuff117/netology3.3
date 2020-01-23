from urllib.parse import urlencode
from pprint import pprint
import requests

OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': 7279354,
    # 'redirect_uri':
    'display': 'popup',
    'scope': 'friends',
    'response_type': 'token'
}

# print('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))

TOKEN = '698d2bc404e1b505cd841025f5f640005ff34899ffa32eb4fe065438e4708aaaf45b82700d9bcedfd82ef'

# params = {
#     'access_token': TOKEN,
#     'v': 5.8,
#     'fields': 'first_name',
#     'order': 'name'
# }

# response = requests.get(
#     'https://api.vk.com/method/friends.get',
#     params
# )
# pprint(response.json())


class UserVk:
    def __init__(self, id):
        self.id = id
        params = {
    'access_token': TOKEN,
    'v': 5.89,
    'user_ids': self.id }

        response_user = requests.get('https://api.vk.com/method/users.get?', urlencode(params))
        user_info = response_user.json()
        # print(user_info)

user1= UserVk('45255933')