from django.http import Http404
from rest_framework import generics

from rss.models import Rate
from rss.serializers import RateSerializer


class RatesList(generics.ListAPIView):
    serializer_class = RateSerializer
    queryset = Rate.objects.all().order_by('-store_date')


class RateDetail(generics.ListAPIView):
    serializer_class = RateSerializer

    def get_queryset(self):
        iso = self.kwargs.get('iso')
        queryset = Rate.objects.filter(iso=iso).order_by('-store_date')
        if queryset.count() < 1:
            raise Http404()

        return queryset
