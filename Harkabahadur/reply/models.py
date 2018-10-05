from django.db import models


class response(models.Model):
    name = models.CharField(max_length=200)
    values = models.CharField(max_length=200)


class log(models.Model):
    selectedButtonId = models.CharField(max_length=20)
    timeValue = models.CharField(max_length=20)
    tolerance = models.CharField(max_length=20)
    timeStamp = models.CharField(max_length=20)

    def __str__(self):
        return 'TIMESTAMP: ' + self.timeStamp