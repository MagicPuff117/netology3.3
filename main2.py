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

TOKEN = '479d9ac76dc1d3d74e6731642a5cf78256d32171f64623cb1c84f85a324557cfd323d4bee92ad112a6b07'


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
    def __init__(self, id, ):
        self.id = id  # id Вконтакте
        user = {
            'access_token': TOKEN,
            'v': 5.89,
            'user_ids': self.id,
            # 'fields': 'nickname'
        }

        response_user = requests.get('https://api.vk.com/method/users.get?', urlencode(user))
        user_info = response_user.json()
        self.first_name, self.last_name = user_info['response'][0]['first_name'], user_info['response'][0]['last_name']
        # pprint(self.first_name)
        response_friends = requests.get('https://api.vk.com/method/friends.get?', urlencode(user))
        friends_info = response_friends.json()
        # pprint(friends_info)
        self.friend_list = friends_info['response']['items']
        # pprint(self.friend_list)

        try:
            self.friend_list = friends_info['response']['items']
        except KeyError:
            self.friend_list = []

    def __and__(self, other):
        self_friends = set(self.friend_list)
        other_friends = set(other.friend_list)
        mutual_friends = self_friends.intersection(other_friends)
        # pprint(mutual_friends)
        users_list = []
        counter = 0

        for friend in mutual_friends:
            counter += 1
            print(f'Общих друзей найдено: {counter}')
            user = VkUser(friend)
            time.sleep(1)
            users_list.append(user)
        return users_list

    def __str__(self):
        string = f'ID: {self.id}\nИмя: {self.first_name}\nФамилия: {self.last_name}\n***\n'
        return string


first_user = VkUser(107151055)
second_user = VkUser(17460386)
mutual_list = first_user & second_user

print(f'\nОбщие друзья для {first_user.first_name} {first_user.last_name} и {second_user.first_name} {second_user.last_name}:\n')
for user in mutual_list:
    print(user)


# user1 = VkUser(17460386)  # 17460386 - мой id

# user1.get_friends_list()
