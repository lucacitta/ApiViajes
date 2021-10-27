from django.db import models
from django.db.models.deletion import CASCADE
from apps.destinations.models import Destination

class Travel(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    destination = models.ForeignKey(Destination, on_delete=CASCADE)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'travel'
        verbose_name_plural = 'travels'

    def __str__(self):
        return str(f'Travel ID: {self.id}, Destination: {self.destination}')

class Passanger(models.Model):
    Birth_date = models.DateField()
    document_id = models.IntegerField(unique=True)
    type_of_document = models.CharField(max_length=20)
    gender = models.CharField(max_length=30)
    travel = models.ManyToManyField(Travel)

    class Meta:
        verbose_name = 'passanger'
        verbose_name_plural = 'passangers'

    def __str__(self):
        return str(self.document_id)


