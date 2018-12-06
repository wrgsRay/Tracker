"""
Python Version 3.7.1
Author: wrgsRay
"""

import requests
from bs4 import BeautifulSoup as bs


class USPS:
    def __init__(self, awb):
        self.awb = awb

    def status_latest(self):
        url = 'https://tools.usps.com/go/TrackConfirmAction?tLabels=' + self.awb
        agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
        headers = {'user-agent': agent}
        res = requests.get(url, headers=headers)
        try:
            res.raise_for_status()
            soup = bs(res.text, 'html.parser')
        except Exception as e:
            print(e)
        title = soup.title.getText()
        return title


def main():
    package_1 = USPS('9405511699000799152259')
    print(package_1.awb)
    print(package_1.status_latest())


if __name__ == '__main__':
    main()
else:
    pass
# pass