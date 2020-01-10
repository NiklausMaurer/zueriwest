#! /usr/bin/env python

import requests
from geotext import GeoText


def getCities(url):
    r = requests.get(url, allow_redirects=True)
    places = GeoText(r.text)
    print(url)
    print(places.cities)


def main():
    getCities("https://www.hunold.ch/zw/zueriwest.html")
    getCities("https://www.hunold.ch/zw/goeteborg.html")
    getCities("https://www.hunold.ch/zw/homerekords.html")
    getCities("https://www.hunold.ch/zw/haubi.html")
    getCities("https://www.hunold.ch/zw/aloha.html")
    getCities("https://www.hunold.ch/zw/zwretour.html")
    getCities("https://www.hunold.ch/zw/rzg.html")
    getCities("https://www.hunold.ch/zw/super8.html")
    getCities("https://www.hunold.ch/zw/hooverjam.html")
    getCities("https://www.hunold.ch/zw/wintertour.html")
    getCities("https://www.hunold.ch/zw/arturobandini.html")
    getCities("https://www.hunold.ch/zw/elvis.html")
    getCities("https://www.hunold.ch/zw/buempliz.html")
    getCities("https://www.hunold.ch/zw/sportmusik.html")


if __name__ == "__main__":
    main()
