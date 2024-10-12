from django.db import models


class Interest(models.Model):
    interest = models.CharField(max_length=30)

    def __str__(self):
        return self.interest


# record = Interest(interest="IT")
# record.save()