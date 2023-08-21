from django.db import models

# Create your models here.
class ckdModel(models.Model):

    age=models.FloatField()
    bmi=models.FloatField()
    smoker_yes=models.FloatField()
