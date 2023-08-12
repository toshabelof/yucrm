import requests

import _log
from realty.realty import Realty

URL_STATIONS = '/realty.address.stations'


class Stations(Realty):
    def __init__(self, yu_crm=None):
        super().__init__(url=URL_STATIONS, login=yu_crm.login, token=yu_crm.token)

    def List(self, page=None, limit=None, mode=None, order_by=None, order_dir=None,
             id=None, created_at=None, updated_at=None, name=None, is_metro=None, metro_id=None):
        request = f'{self.__full_url()}/list'
        params = {'page': page, 'limit': limit, 'mode': mode, 'order_by': order_by, 'order_dir': order_dir,
                  'id': id, 'created_at': created_at, 'updated_at':updated_at, 'name': name,
                  'is_metro': is_metro, 'metro_id': metro_id}
        _log.logg(f'Get request {request}, params={params}')

        return requests.get(request, params=params)
