from django.db import models

# Create your models here.
class competition (models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    # active = models.BooleanField()
    def __str__(self):
        return f"{self.name} {self.start_date}"