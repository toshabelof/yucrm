from realty.realty import Realty

URL_REPAIR_TYPES = '/realty.address.regions'


class RepairTypes(Realty):
    def __init__(self, yu_crm=None):
        super().__init__(url=URL_REPAIR_TYPES, login=yu_crm.login, token=yu_crm.token)
