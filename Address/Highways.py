from realty.realty import Realty

URL_HIGHWAYS = '/realty.address.highways'


class Highways(Realty):
    def __init__(self, yu_crm=None):
        super().__init__(url=URL_HIGHWAYS, login=yu_crm.login, token=yu_crm.token)
