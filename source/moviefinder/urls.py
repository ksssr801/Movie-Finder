from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import dump_movie_to_database, get_movie_list, get_movie_detail

router = DefaultRouter()
urlpatterns = router.urls
urlpatterns.append(url(r'dump-movie-to-database', dump_movie_to_database))
urlpatterns.append(url(r'movies-list', get_movie_list))
urlpatterns.append(url(r'movie-detailed-list/(?P<imdb_id>[^/.]+)', get_movie_detail, name='movie_detail'))
# urlpatterns.append(url(r'parking-lot-current-status', get_parking_lot_status))
