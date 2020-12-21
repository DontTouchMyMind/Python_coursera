import requests
import pprint


def get_location_info():
    return requests.get('https://freegeoip.app/json/').json()



if __name__ == '__main__':
    pprint.pprint(get_location_info())

    p = 'привет'
    print(p[0:1])
    pi = 3.1415926
    pi_fmt = f"{pi:#0.2f}"
    print(type(pi_fmt))