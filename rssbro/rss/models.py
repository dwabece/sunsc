from django.db import IntegrityError, models


class Rate(models.Model):
    iso = models.CharField(max_length=4)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    store_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)

    @classmethod
    def ingest(cls, date, rates):
        for (curr, value) in rates.items():
            try:
                cls.objects.create(iso=curr, value=value, store_date=date)
            except IntegrityError:
                break

    class Meta:
        unique_together = ('iso', 'store_date', )
