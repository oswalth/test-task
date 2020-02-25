from config import ACCESS_TOKEN
import requests


selector = """
Enter social network to work with:
'vk' - For vkontakte
'q' - Close app
"""


class SocialNetworkConnector:

    methods = {
        'vk': {
            'user': 'https://api.vk.com/method/users.get?user_ids={user_id}&v=5.52&access_token={token}',
            'user friends': 'https://api.vk.com/method/friends.get?user_id={user_id}&order=name&fields=city%2Cdomain%2Cphoto_50&v=5.52&access_token={token}',
            'user wall': 'https://api.vk.com/method/wall.get?owner_id={user_id}&extended=1&count=5&v=5.52&access_token={token}'}}

    def __init__(self, social_network):
        self.social_network = social_network
        self.start()

    def start(self):
        while True:
            action = input("""Specify action to perform: +
            'user' - Get user info by id or username
            'user friends' - List user friends
            'user wall' - Get user posts
            'q' - Close connection
            """)
            keys = list(self.methods.keys())
            if action not in list(self.methods[self.social_network].keys()):
                if action == 'q':
                    break
                continue
            user_id = input('Enter user id: ')
            self.procees_request(action, user_id)

    def procees_request(self, action, id):
        if not id.isdigit():
            response = requests.get(self.methods[self.social_network]['user'].format(
                user_id=id, token=ACCESS_TOKEN)).json()
            id = response['response'][0]['id']
        response = requests.get(self.methods[self.social_network][action].format(
            user_id=id, token=ACCESS_TOKEN))
        print(response.json())


if __name__ == '__main__':
    while True:
        social_network = input(selector)
        keys = list(SocialNetworkConnector.methods.keys())
        a = social_network in keys
        if not social_network in list(SocialNetworkConnector.methods.keys()):
            if social_network == 'q':
                break
            continue
        scn = SocialNetworkConnector(social_network)
