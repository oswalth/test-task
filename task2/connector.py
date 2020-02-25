from config import ACCESS_TOKEN
import requests


class SocialNetworkConnector:

    methods = {
        'vk': {
            'user': 'https://api.vk.com/method/users.get?user_ids={user_id}&v=5.52&access_token={token}',
            'user friends': 'https://api.vk.com/method/friends.get?user_id={user_id}&order=name&fields=city%2Cdomain%2Cphoto_50&v=5.52&access_token={token}',
            'user wall': 'https://api.vk.com/method/wall.get?owner_id={user_id}&extended=1&count=5&v=5.52&access_token={token}'
        }
    }

    def __init__(self, social_network):
        self.social_network = social_network

    
    def procees_request(self, action, id):
        if not id.isdigit():
            response = requests.get(self.methods[self.social_network]['user'].format(user_id=id, token=ACCESS_TOKEN)).json()
            id = response['response'][0]['id']
        response = requests.get(self.methods[self.social_network][action].format(user_id=id, token=ACCESS_TOKEN))
        print(response.json())




scn = SocialNetworkConnector('vk')
scn.procees_request('user', 'fkirkorov')