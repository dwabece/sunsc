"""Set of celery tasks"""
from rss import feed
from rss.models import Rate
from rssbro.celery import app


@app.task
def fetch():
    """
    Task that fetches latest exchange and stores it
    to the DB

    """
    date, fetched_data = feed.fetch_exchange_feed()
    Rate.ingest(date, fetched_data)
