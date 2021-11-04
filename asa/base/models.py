from django.db import models

class Tournoi(models.Model):
    name = models.CharField(max_length=50)
    lieu = models.CharField(max_length=50)
    date = models.DateField()
    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name[0:10]

    class Meta:
        ordering = ['-updated']
