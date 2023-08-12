from realty.realty import Realty

URL_DISTRICTS = '/realty.address.districts'


class Districts(Realty):
    def __init__(self, yu_crm=None):
        super().__init__(url=URL_DISTRICTS, login=yu_crm.login, token=yu_crm.token)
