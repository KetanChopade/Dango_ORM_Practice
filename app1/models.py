from django.db import models

class Person(models.Model):                                #class created
    idno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, blank=True)


    def __str__(self):                                      #dundar
        return self.name