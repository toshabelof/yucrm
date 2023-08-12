from realty.realty import Realty


URL_DEPOSITS = '/realty.lists.deposits'


class Deposits(Realty):
    def __init__(self, yu_crm=None):
        super().__init__(url=URL_DEPOSITS, login=yu_crm.login, token=yu_crm.token)
