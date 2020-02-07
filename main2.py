from urllib.parse import urlencode
from pprint import pprint
import requests
import time

OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': 7279354,
    # 'redirect_uri':
    'display': 'popup',
    'scope': 'friends',
    'response_type': 'token'
}

print('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))


TOKEN = '74107cc39fd8c1b58240bc160590c704f8568b3d768666218277525b78f6fff0bef806956db0f15afd01f'


# params = {
#     'access_token': TOKEN,
#     'v': 5.8,
#     'fields': 'first_name',
#     'order': 'name'
# }
#
# response = requests.get(
#     'https://api.vk.com/method/friends.get',
#     params
# )
# pprint(response.json())

class VkUser:
    def __init__(self, id):
        self.id = id # id Вконтакте
        params = {
            'access_token': TOKEN,
            'v': 5.8,
            'user_id': self.id,
            'fields' : 'nickname'
            }

        response_user = requests.get('https://api.vk.com/method/friends.get?', urlencode(params))
        user_info = response_user.json()
        self.first_name, self.last_name = user_info['response'][0]['first_name'], user_info['response'][0]['last_name']
        # print(self.first_name)
        response_friends = requests.get('https://api.vk.com/method/friends.get?', urlencode(params))
        friends_info = response_friends.json()
        # print(friends_info)
        self.friend_list = friends_info['response']['items']


user1 = VkUser(17460386)  # 17460386 - мой id

# user1.get_friends_list()


