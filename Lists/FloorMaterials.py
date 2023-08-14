from realty.realty import Realty


URL_FLOOR_MATERIALS = '/realty.lists.floor_materials'


class FloorMaterials(Realty):
    def __init__(self, yu_crm=None):
        super().__init__(url=URL_FLOOR_MATERIALS, login=yu_crm.login, token=yu_crm.token)
