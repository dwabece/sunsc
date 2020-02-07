from decimal import Decimal

from rss import feed


def test_curencize():
    assert feed.currencize('123.9889123') == Decimal('123.99')
