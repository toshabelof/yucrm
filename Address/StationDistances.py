from realty.realty import Realty

URL_STATION_DISTANCES = '/realty.address.station_distances'


class StationDistances(Realty):
    def __init__(self, yu_crm=None):
        super().__init__(url=URL_STATION_DISTANCES, login=yu_crm.login, token=yu_crm.token)
