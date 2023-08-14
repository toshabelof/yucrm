from realty.realty import Realty

URL_OWNER_SHIPS = '/realty.address.regions'


class OwnerShips(Realty):
    def __init__(self, yu_crm):
        super().__init__(url=URL_OWNER_SHIPS, login=yu_crm.login, token=yu_crm.token)
