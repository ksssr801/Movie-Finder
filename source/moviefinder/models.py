from __future__ import unicode_literals
from django.db import models

# Models not required, using file system

# class MovieInfo(models.Model):
#     movie_id = models.AutoField(primary_key=True, db_column='movie_id')
#     title = models.CharField(max_length=500, null=False)
#     plot = models.CharField(max_length=500, null=True)
#     writer = models.CharField(max_length=500, null=True)
#     director = models.CharField(max_length=500, null=True)
#     production = models.CharField(max_length=500, null=True)
#     awards = models.CharField(max_length=500, null=True)
#     language = models.CharField(max_length=500, null=True)
#     box_office = models.CharField(max_length=500, null=True)
#     runtime = models.CharField(max_length=500, null=True)
#     actors = models.CharField(max_length=500, null=True)
#     poster_url = models.TextField()
#     genre = models.CharField(max_length=500, null=True)
#     release_date = models.CharField(max_length=500, null=True)
#     imdb_rating = models.FloatField(default=0)
#     imdb_votes = models.IntegerField(default=0)

#     class Meta:
#         db_table = 'tblmovieinfo'

# class ImdbIdInfo(models.Model):
#     imdb_id = models.CharField(max_length=500, null=False)

#     class Meta:
#         db_table = 'tblimdbidinfo'