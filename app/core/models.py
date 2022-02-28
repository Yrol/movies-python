from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return '%s %s' % (self.name, self.description)

class Movies(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    genre = models.ForeignKey(Genre, related_name='genre', null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s %s %s' % (self.name, self.description, self.genre, self.rating)