from time import sleep

import requests


def pull_rolls():
    url = 'https://tubedl.herokuapp.com/ping'
    requests.get(url)
    print('pulled')


def main():
    while True:
        pull_rolls()
        sleep(1)


if __name__ == '__main__':
    main()
else:
    main()
