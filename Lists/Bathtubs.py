from realty.realty import Realty


URL_BATHTUBS = '/realty.lists.bathtubs'


class FloorMaterials(Realty):
    def __init__(self, yu_crm=None):
        super().__init__(url=URL_BATHTUBS, login=yu_crm.login, token=yu_crm.token)
