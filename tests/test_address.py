import _log
from Address.Cities import Cities
from Address.Districts import Districts
from yucrm import YuCRM

crm = YuCRM('belovstech', 'b20e619ab772f294fba8ad6aa160b1f8')


def test_cities():
    city = Cities(crm)
    _log.logg(city.List().json())
    _log.logg(city.List(id=8055).json())
    _log.logg(city.Get(id=1).json())


def test_districts():
    districts = Districts(crm)
    _log.logg(districts.List().json())
    _log.logg(districts.List(id=8055).json())
    _log.logg(districts.Get(id=1).json())


if __name__ == '__main__':
    _log.logg('Start testing object "Cities"')
    test_cities()
    _log.logg('Start testing object "Districts"')
    test_districts()
