URL = 'https://{login}.yucrm.ru/api/v1/{token}'


class YuCRM:
    def __init__(self, login, token):
        self.__login = login
        self.__token = token
        self._url = URL

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token):
        self.__token = token

    @property
    def url(self):
        return self._url
