import datetime
from decimal import Decimal

import requests
from django.conf import settings
from lxml import etree


def fetch_exchange_feed():
    """
    Fetch RSS feed with latest exchange

    :return: date and exchange dict
    :rtype: tuple
    """
    resp = requests.get(settings.FEED_URL, stream=True, timeout=1.5)
    resp.raise_for_status()

    namespaces = {'ex': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'}
    xmltree = etree.fromstring(resp.content)
    date_entry = xmltree.find('.//ex:Cube[@time]', namespaces=namespaces)
    rates = xmltree.findall('.//ex:Cube[@currency]', namespaces=namespaces)

    currencies = {curr.attrib['currency']: currencize(curr.attrib['rate']) for curr in rates}

    return convert_date(date_entry.attrib['time']), currencies


def convert_date(date_str):
    """
    Map string with date to date obj

    :param date_str: string containing date
    :rtype: date object
    """
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()


def currencize(value):
    """
    Converts exchange values to propper format

    """
    return Decimal(value).quantize(Decimal('0.00'))
