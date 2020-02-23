from django.db import models

# Create your models here.


class ActorModel(models.Model):
    id_actor = models.AutoField(primary_key=True)
    name_actor = models.CharField(max_length=255)
    detail_actor = models.TextField()
    age_actor = models.IntegerField(default=0)
