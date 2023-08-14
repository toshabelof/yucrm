import requests

from Constants import Compare
import _log
from CustomExceptions import InvalidCondition

URL_REALTY = 'https://{login}.yucrm.ru/api/v1/{token}'


class Realty:
    def __init__(self, url, login, token):
        self._url = url
        self._login = login
        self._token = token

    def _full_url(self):
        return f'{URL_REALTY.format(login=self._login, token=self._token)}{self._url}'

    def List(self, page=None, limit=None, mode=None, order_by=None, order_dir=None, condition=None,
             id=None, name=None):
        if condition is not None and condition.name not in list(map(lambda c: c.name, Compare)):
            raise InvalidCondition

        request = f'{self._full_url()}/list'
        params = {'page': page, 'limit': limit, 'mode': mode, 'order_by': order_by, 'order_dir': order_dir,
                  'id' + f'[{condition.value}]' if condition is not None else '': id,
                  'name' + f'[{condition.value}]' if condition is not None else '': name}
        _log.logg(f'Get request {request}, params={params}')

        return requests.get(request, params=params)

    def Get(self, id):
        request = f'{self._full_url()}/get/{id}'
        _log.logg(f'Get request {request}')

        return requests.get(request)

    def Update(self, id, params):
        request = f'{self._full_url()}/update/{id}'
        _log.logg(f'Get request {request}, params={params}')

        return requests.get(request, params=params)

    def Add(self, params):
        request = f'{self._full_url()}/add'
        _log.logg(f'Get request {request}, params={params}')

        return requests.get(request, params=params)
