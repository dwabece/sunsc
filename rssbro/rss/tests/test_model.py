from datetime import date
from decimal import Decimal

import pytest
from rss.models import Rate


@pytest.mark.django_db
def test_rate_ingest():
    data = {
        'CZK': Decimal('42.69'),
        'CAD': Decimal('69.96')
    }
    today_date = date.today()

    Rate.ingest(today_date, data)

    assert Rate.objects.count() == 2
