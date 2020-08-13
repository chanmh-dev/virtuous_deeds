from django.db import models

# Create your models here.


class deeds(models.Model):
    deed = models.CharField(max_length=500)
    name = models.CharField(max_length=80)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name        
