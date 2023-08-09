from datetime import datetime


def logg(text):
    print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}: {text}')