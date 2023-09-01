import json
from room import Room


class Radio(Room):
    def __init__(self, client, room_id, type=None, artist=None, title=None, audio_id=None, audio_owner_id=None, duration=None):
        super().__init__(client)

        self.type = type
        self.artist = artist
        self.title = title
        self.audio_owner_id = audio_owner_id
        self.audio_id = audio_id
        self.duration = duration
        self.room_id = room_id

        if artist:
            self.radio_add()

    def radio_add(self):
        data = {
            'type': self.type,
            'artist': self.artist,
            'title': self.title,
            'audioOwnerId': self.audio_owner_id,
            'audioId': self.audio_id,
            'duration': self.duration
        }

        return self.client.room.radio_add(self.room_id, data)

    def radio_vote(self, vote):
        return self.client.room.radio_vote(self.room_id, vote)
