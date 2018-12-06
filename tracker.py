"""
Python Version 3
Author: wrgsRay
"""
from bs4 import BeautifulSoup as bs
import requests


class USPS:
    def __init__(self, awb):
        self.awb = awb
        self.url = 'https://tools.usps.com/go/TrackConfirmAction?tLabels=' + self.awb
        self.agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
        self.headers = {'user-agent': self.agent}
        self.current_status = ''

    def get_status(self):
        global html
        global soup
        res = requests.get(self.url, headers=self.headers)
        try:
            res.raise_for_status()
            html = res.text
            soup = bs(html, 'html.parser')
        except Exception as e:
            print(e)

    def status_latest(self):
        self.current_status = soup.select_one('h2 > strong').string if (soup.select_one('h2 > strong') is not None) \
            else 'Not Found'
        return self.current_status

    def detailed_status(self):
        result = list()
        if self.current_status == 'Delivered':
            return 'No more info available for delivered packages'
        elif not soup.find(attrs={"class": "status_feed"}):
            for string in soup.find(attrs={"class": "status_feed"}).stripped_strings:
                result.append(string)
            result_time = ' '.join(result[0].split())
            result_status = result[1]
            result_location = result[2]
            return f'As of {result_time}, the package {result_status} and the last know location is {result_location}'
        else:
            return "Element not found"


def main():
    package_1 = USPS('9405511699000796228506')
    print(package_1.awb)
    package_1.get_status()
    print(package_1.status_latest())
    print(package_1.detailed_status())
    # package_2 = USPS('LT074946082CN')
    # print(package_2.awb)
    # package_2.get_status()
    # print(package_2.status_latest())
    # print(package_2.detailed_status())
    # package_3 = USPS('LT000264475CN')
    # print(package_3.awb)
    # package_3.get_status()
    # print(package_3.status_latest())
    # print(package_3.detailed_status())


if __name__ == '__main__':
    main()
else:
    pass
