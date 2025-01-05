from django.db import models

# Create your models here.
class storedatamodel(models.Model):
    #id = models.CharField(max_length=500)
    label = models.CharField(max_length=300)
    tweet = models.CharField(max_length=300)

    def __str__(self):
        return self.label, self.tweet