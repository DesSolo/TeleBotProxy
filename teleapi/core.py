import os
import requests


def input_file_or_string(**kwargs):
    data = {}
    files = {}
    for key, value in kwargs.items():
        if not os.path.isfile(value):
            data[key] = value
        else:
            with open(value, 'rb') as file:
                files[key] = file.read()
    return data, files


class TelegramApi:
    def __init__(self, token, proxy=None):
        """
        :param token: telegram token
        :param proxy: proxy param:
                'socks5://ip:port'
                'socks5h://ip:port'
                'http://user:pass@ip:port'
        """
        self.url = f'https://api.telegram.org/bot{token}/'
        self.session = requests.Session()
        if proxy:
            self.session.proxies = {'https': proxy}

    def raw(self, method, uri, params=None, data=None, files=None):
        """
        Low level method send request
        :param method: get | post | put
        :param uri: sub url without protocol and domain name
        :param params: query params
        :param data: data params
        :param files: upload files
        :return:
        """
        return self.session.request(method, self.url + uri, params=params, data=data, files=files)

    def send_message(self, chat_id, text, **kwargs):
        """https://core.telegram.org/bots/api#sendmessage"""
        data = {
            'chat_id': chat_id,
            'text': text,
            **kwargs
        }
        return self.raw('post', 'sendMessage', data=data)

    def forward_message(self, chat_id, from_chat_id, message_id, **kwargs):
        """https://core.telegram.org/bots/api#forwardmessage"""
        data = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id,
            **kwargs
        }
        return self.raw('post', 'forwardMessage', data=data)

    def send_photo(self, chat_id, photo, **kwargs):
        """https://core.telegram.org/bots/api#sendphoto"""
        data, files = input_file_or_string(photo=photo)
        data.update(chat_id=chat_id, **kwargs)
        return self.raw('post', 'sendPhoto', data=data, files=files)

    def send_audio(self, chat_id, audio, **kwargs):
        """https://core.telegram.org/bots/api#sendaudio"""
        data, files = input_file_or_string(audio=audio)
        data.update(chat_id=chat_id, **kwargs)
        return self.raw('post', 'sendAudio', data=data)

    def send_document(self, chat_id, document, **kwargs):
        """https://core.telegram.org/bots/api#senddocument"""
        data, files = input_file_or_string(document=document)
        data.update(chat_id=chat_id, **kwargs)
        return self.raw('post', 'sendDocument', data=data, files=files)

    def send_video(self, chat_id, video, **kwargs):
        """https://core.telegram.org/bots/api#sendvideo"""
        data, files = input_file_or_string(video=video)
        data.update(chat_id=chat_id, **kwargs)
        return self.raw('post', 'sendVideo', data=data, files=files)

    def send_animation(self, chat_id, animation, **kwargs):
        """https://core.telegram.org/bots/api#sendvideo"""
        data, files = input_file_or_string(animation=animation)
        data.update(chat_id=chat_id, **kwargs)
        return self.raw('post', 'sendAnimation', data=data, files=files)

    def send_voice(self, chat_id, voice, **kwargs):
        """https://core.telegram.org/bots/api#sendvoice"""
        data, files = input_file_or_string(voice=voice)
        data.update(chat_id=chat_id, **kwargs)
        return self.raw('post', 'sendVoice', data=data, files=files)

    def send_video_note(self, chat_id, video_note, **kwargs):
        """https://core.telegram.org/bots/api#sendvideonote"""
        data, files = input_file_or_string(video_note=video_note)
        data.update(chat_id=chat_id, **kwargs)
        return self.raw('post', 'sendVideoNote', data=data, files=files)
