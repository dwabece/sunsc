from django.core.management.base import BaseCommand

from rss import feed
from rss.models import Rate


class Command(BaseCommand):
    help = 'Ingests rates from rss'

    def handle(self, *args, **kwargs):
        date, fetched_data = feed.fetch_exchange_feed()
        Rate.ingest(date, fetched_data)
