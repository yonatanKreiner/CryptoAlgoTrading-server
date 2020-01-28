from pushbullet import Pushbullet

API_KEY = 'API_KEY'

class PushbulletClient:
    def __init__(self):
        self.__pb = Pushbullet(API_KEY)

    def push(self, agent, event):
        self.__pb.push_note(agent, event)
