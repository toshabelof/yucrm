import requests
from requests import Response

import _log
from yucrm import YuCRM

URL_REGIONS = '/realty.address.regions'


class Regions(YuCRM):
    def __init__(self, yu_crm):
        super().__init__(yu_crm.login, yu_crm.token)

    def __full_url(self):
        return f'{super().url.format(login=super().login, token=super().token)}{URL_REGIONS}'

    def List(self, id=None, name=None, page=None, limit=None, mode=None, order_by=None, order_dir=None) -> Response:
        url = f'{self.__full_url()}/list'
        params = {'page': page, 'limit': limit, 'mode': mode, 'order_by': order_by, 'order_dir': order_dir, 'id': id,
                  'name': name}
        _log.logg(f'Get request {url}, params={params}')

        result = requests.get(url, params=params)
        return result

    def Get(self, id) -> Response:
        url = f'{self.__full_url()}/get/{id}'
        _log.logg(f'Get request {url}')

        result = requests.get(url)
        return result

    def Update(self, id, params) -> Response:
        url = f'{self.__full_url()}/update/{id}'
        _log.logg(f'Get request {url}, params={params}')

        result = requests.get(url, params=params)
        return result

    def Add(self, params) -> Response:
        url = f'{self.__full_url()}/add'
        _log.logg(f'Get request {url}, params={params}')

        result = requests.get(url, params=params)
        return result