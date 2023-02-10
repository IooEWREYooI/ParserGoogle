# -*- coding: cp1251 -*-
from bs4 import BeautifulSoup
import urllib.request


def getTable():
    contents = urllib.request.urlopen("https://confluence.hflabs.ru/pages/viewpage.action?pageId=1181220999").read()
    soup = BeautifulSoup(contents, 'lxml')
    table = soup.table
    head = table.findAll('th')
    str = ''
    for header in head:
        str += header.text + '\n'
    body = table.findAll('td')
    for bodies in body:
        str += bodies.text + '\n'

    return str
