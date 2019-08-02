from django.db import models


# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=55)
    number = models.BigIntegerField()

    def __str__(self):
        return self.name + '  -   ' + str(self.number)


