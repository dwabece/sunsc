from rest_framework import serializers

from rss.models import Rate


class RateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rate
        fields = ['iso', 'value', 'store_date']
