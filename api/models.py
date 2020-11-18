from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    score = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)
