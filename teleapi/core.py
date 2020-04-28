import os
import requests


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
        if not os.path.isfile(photo):
            data = {
                'chat_id': chat_id,
                'photo': photo,
                **kwargs
            }
            return self.raw('post', 'sendPhoto', data=data)
        with open(photo, 'rb') as file:
            data = {
                'chat_id': chat_id,
                **kwargs
            }
            files = {
                "photo": file.read()
            }
            return self.raw('post', 'sendPhoto', data=data, files=files)

