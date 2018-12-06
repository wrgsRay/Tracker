"""
Python Version 3.7.1
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
        self.html = ''
        # TODO: do requests and soup in init

    def status_latest(self):
        global soup
        res = requests.get(self.url, headers=self.headers)
        try:
            res.raise_for_status()
            self.html = res.text
            soup = bs(self.html, 'html.parser')
        except Exception as e:
            print(e)
        current_status = soup.select_one('h2 > strong').string if (soup.select_one('h2 > strong') is not None) \
            else 'Not Found'
        return current_status

    @staticmethod
    def detailed_status():
        result = list()
        # TODO: Solve the issue if the tracking is invalid or empty
        if soup.find(attrs={"class": "status_feed"}) is not None:
            for string in soup.find(attrs={"class": "status_feed"}).stripped_strings:
                result.append(string)
            result_time = ' '.join(result[0].split())
            result_status = result[1]
            result_location = result[2]
            return f'As of {result_time}, the package {result_status} and the last know location is {result_location}'
        else:
            return "Element not found"


def main():
    package_1 = USPS('9405511699000799152259')
    print(package_1.awb)
    print(package_1.status_latest())
    print(package_1.detailed_status())


if __name__ == '__main__':
    main()
else:
    pass
