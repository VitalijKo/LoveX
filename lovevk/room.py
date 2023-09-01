import json


class Room:
    def __init__(self, client):
        self.client = client
        self.api = 'room/v3/'
        self.queue: Queue = Queue(self)
        self.chat: Chat = Chat(self)
        self.private_rooms = PrivateRooms(self)

    def get_room(self, room_id=None, area_id=None, force=True, is_switch=True):
        data = {
            'pc_fingerprint': self.client.pc_fingerprint,
            'is_mobi': self.client.mobi,
            'force': force,
            'is_switch': is_switch
        }

        if room_id:
            data['target_room_id'] = f'{self.client.room_iders}_{room_id}'

        if area_id:
            data['area_id'] = area_id

        return self.client.request(f'{self.api}getRoom.php', _data=data)

    def get_room_list(self, ids=None, sex=2, age=17):
        data = {
                'ids': ids,
                'sex': sex,
                'age': age
        } if ids else {}

        return self.client.request('room/v3/getRoomList.php', _data=data)

    def exit(self, room_id):
        data = {
            'r': f'{self.client.room_iders}_{room_id}'
        }

        return self.client.request(f'{self.api}exit.php', _data=data)

    def get_user_ids(self, room_id):
        data = {
            'r': f'{self.client.room_iders}_{room_id}'
        }

        return self.client.request(f'{self.api}getUids.php', _data=data)

    def kick_user(self, room_id, target_uid, reason_id=1, anon=True, price=1):
        data = {
            'reasonId': reason_id,
            'roomId': f'{self.client.room_iders}_room_id',
            'anon': anon,
            'target_uid': target_uid,
            'price': price
        }

        return self.client.request(f'{self.api}kick.php', _data=data)

    def resque_user(self, room_id, target_uid, price=1):
        data = {
            'r': f'{self.client.room_iders}_{room_id}',
            'uid': target_uid,
            'price': price
        }

        return self.client.request(f'{self.api}resque.php', _data=data)

    def add_answer(self, room_id, answer, question):
        data = {
            'r': f'{self.client.room_iders}_{room_id}',
            'a': answer,
            'q': question
        }

        return self.client.request(f'{self.api}addAnswer.php', _data=data)

    def user_toggle_block(self, room_id, target_uid, value):
        data = {
            'r': f'{self.client.room_iders}_{room_id}',
            'target_uid': target_uid,
            'value': value
        }

        return self.client.request(f'{self.api}toggleBlock.php', _data=data)

    def radio_vote(self, room_id, vote):
        data = {
            'vote': vote,
            'r': f'{self.client.room_iders}_{room_id}'
        }

        return self.client.request(f'{self.api}radio/vote.php', _data=data)

    def radio_add(self, room_id, track, price=0):
        data = {
            'r': f'{self.client.room_iders}_{room_id}',
            'track': json.dumps(track),
            'price': price
        }

        return self.client.request(f'{self.api}radio/add.php', _data=data)

    def radio_remove(self, room_id, id):
        data = {
            'id': id,
            'r': f'{self.client.room_iders}_{room_id}'
        }

        return self.client.request(f'{self.api}radio/remove.php', _data=data)

    def add_game_gift(self, room_id, target_uid, gift_id, coords, count=1, action_id=1, v=1):
        data = {
            'r': f'{self.client.room_iders}_{room_id}',
            'v': v,
            'target_uid': target_uid,
            'gift_id': gift_id,
            'coordsJson': json.dumps(coords),
            'count': count,
            'action_id': action_id
        }

        return self.client.request(f'{self.api}addGameGift.php', 'post', _data=data)

    def add_bot(self, room_id, sex, by_one=True):
        data = {
            'r': f'{self.client.room_iders}_{room_id}',
            'bot_sex': sex,
            'by_one': by_one
        }

        return self.client.request(f'{self.api}addBot.php', _data=data)


class Queue:
    def __init__(self, client):
        self.client = client.client
        self.api = f'{client.api}queue/'

    def buy_place(self, room_id, price=5):
        data = {
            'r': f'{self.client.room_iders}_{room_id}',
            'price': price
        }

        return self.client.request(f'{self.api}buyPlace.php', _data=data)

    def buy_fitst_place(self, room_id):
        data = {
            'r': f'{self.client.room_iders}_{room_id}'
        }

        return self.client.request(f'{self.api}buyFirstPlace.php', _data=data)

    def dismiss_place(self, room_id):
        data = {
            'r': f'{self.client.room_iders}_{room_id}'
        }

        return self.client.request(f'{self.api}dismissPlace.php', _data=data)

    def give_up_place(self, room_id, price, target_uid):
        data = {
            'r': f'{self.client.room_iders}_{room_id}',
            'price': price,
            'target_uid': target_uid
        }

        return self.client.request(f'{self.api}giveUpPlace.php', _data=data)


class Chat:
    def __init__(self, client):
        self.client = client.client
        self.api = f'{client.api}chat/'

    def send_message(self, room_id, message, to=None, reply=None):
        data = {
            'r': f'{self.client.room_iders}_{room_id}',
            'm': message,
            'to': to,
            'reply': reply
        }

        return self.client.request(f'{self.api}add.php', 'post', _data=data)

    def send_sticker(self, room_id, message, config):
        data = {
            'r': f'{self.client.room_iders}_{room_id}',
            'm': message,
            'serialized_config': json.dumps(config)
        }

        return self.client.request(f'{self.api}addSticker.php', 'post', _data=data)

    def new_level(self, exp):
        data = {
            'exp': exp
        }

        return self.client.request(f'{self.api}newLevel.php', _data=data)

    def toggle_like(self, room_id, message_id):
        data = {
            'message_id': message_id,
            'room_id': f'{self.client.room_iders}_{room_id}'
        }

        return self.client.request(f'{self.api}toggleLike.php', _data=data)


class PrivateRooms:
    def __init__(self, client):
        self.client = client.client
        self.api = f'{client.api}private_room/'
