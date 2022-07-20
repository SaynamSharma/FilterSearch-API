from django.db import models


class Specs(models.Model):
    name  = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Mobile(models.Model):
    mobile_name = models.CharField(max_length=100)
    mobile_desc = models.TextField()
    mobile_img = models.TextField()
    price = models.IntegerField()
    specs = models.ManyToManyField(Specs)

    def __str__(self):
        return self.mobile_name

