import Constants
from yucrm import YuCRM
from Lists.Deposits import Deposits


def main():
    crm = YuCRM('belovstech', 'b20e619ab772f294fba8ad6aa160b1f8')
    d = Deposits(crm)
    print(d.List(name='Черт', condition=Constants.Compare.IN).json())


if __name__ == '__main__':
    main()
