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

# print('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))

TOKEN = '3284df561eb4ef353ed161409b9258923335e67a224d94bc858b4ae8a0c0e47c85b182cfab963399707d3'

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


class UserVk:
    def __init__(self, id):
        self.id = id
        params = {
    'access_token': TOKEN,
    'v': 5.89,
    'user_ids': self.id }

        response_user = requests.get('https://api.vk.com/method/users.get?', urlencode(params))
        user_info = response_user.json()
        self.first_name, self.last_name = user_info['response'][0]['first_name'], user_info['response'][0]['last_name']
        # print(self.first_name)
        response_friends = requests.get('https://api.vk.com/method/friends.get?', urlencode(params))
        friends_info = response_friends.json()
        # print(friends_info)
        self.friend_list = friends_info['response']['items']

        try:
            self.friend_list = friends_info['response']['items']
        except KeyError:
            self.friend_list = []

    def __and__(self, other):
        self_friends = set(self.friend_list)
        other_friends = set(other.friend_list)
        mutual_friends = self_friends.intersection(other_friends)
        users_list = []
        counter = 0

        for friend in mutual_friends:
            counter += 1
            print(f'Общих друзей найдено: {counter}')
            user = UserVk(friend)
            # time.sleep(1)
            users_list.append(user)
        return users_list

    def __str__(self):
            string = f'ID: {self.id}\nИмя: {self.first_name}\nФамилия: {self.last_name}\n***\n'
            return string


first_user = UserVk('45255933')
second_user = UserVk('17460386')
mutual_list = first_user & second_user

print(f'\nОбщие друзья для {first_user.first_name} {first_user.last_name} и {second_user.first_name} {second_user.last_name}:\n')
for user in mutual_list:
    print(user)

# user1= UserVk('45255933')