from yucrm import YuCRM
from Address.Regions import Regions


def main():
    crm = YuCRM('guseinov', '1c7d2975ff6e064d393eace4ad6b07f6')
    r = Regions(crm)


if __name__ == '__main__':
    main()
