from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=70)
    available = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    activate = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'destination'
        verbose_name_plural = 'destinations'

    def __str__(self):
        return self.name