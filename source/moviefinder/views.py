# from moviefinder.models import MovieInfo, ImdbIdInfo
# from .serializers import MovieInfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import requests, json


def get_time(original_func):
    import time
    def wrapper_func(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1
        print ('{} function ran in {}'.format(original_func.__name__, t2))
        return result
    return wrapper_func

@get_time
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@renderer_classes([TemplateHTMLRenderer])
def dump_movie_to_database(request):
    final_dict = {}
    imdb_id_list = []
    movie_list = []
    
    f = open('movies_info.dat', 'w')

    # Request to get IMDB Id from API

    # url_for_imdb_id = "https://api.themoviedb.org/3/movie/%s?api_key=16da199820e82c22aefd3c6dede3e0b2"
    # for i in range(101, 151):
    #     resp = requests.get(url=url_for_imdb_id % i)
    #     str_data = resp.text
    #     str_data = str_data.replace('false', 'False')
    #     str_data = str_data.replace('null', 'None')
    #     resp_data = eval(str_data)
    #     imdb_id_list.append(resp_data.get('imdb_id', ''))


    imdb_id_list = [x for x in imdb_id_list if x is not '']
    final_dict.update({'imdb_id_list': imdb_id_list})

    # Request to get Movie Info from API

    # url_for_movie_details = "http://www.omdbapi.com/?i=%s&apikey=5a50670f"
    # for imdb_id in imdb_id_list:
    #     resp = requests.get(url=url_for_movie_details % imdb_id)
    #     str_data = resp.text
    #     resp_data = eval(str_data)
    #     movie_list.append(resp_data)

    final_dict.update({'movie_list': movie_list})
    f.write('%s' % final_dict)
    f.close()

    return Response({}, template_name='dump-to-db-template.html')

@get_time
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@renderer_classes([TemplateHTMLRenderer])
def get_movie_list(request):
    title = str(request.GET.get('title', ''))
    movie_detail_list = []
    f = open('movies_info.dat')
    movie_dataset = eval(f.read())
    f.close()

    movie_list = movie_dataset.get('movie_list')
    for movie in movie_list:
        temp_dict = {}
        temp_dict['imdb_id'] = movie.get('imdbID', '')
        temp_dict['released'] = movie.get('Released', '')
        temp_dict['rating'] = movie.get('imdbRating', '')
        temp_dict['votes'] = movie.get('imdbVotes', '')
        temp_dict['title'] = movie.get('Title', '')
        temp_dict['director'] = movie.get('Director', '')
        temp_dict['production'] = movie.get('Production', '')
        temp_dict['language'] = movie.get('Language', '')
        temp_dict['box_office'] = movie.get('BoxOffice', '')
        temp_dict['runtime'] = movie.get('Runtime', '')
        movie_detail_list.append(temp_dict)

    if title:
        movie_detail_list = filter(lambda x: title.lower() in x.get('title').lower(), movie_detail_list)
    final_dict = {'parking_list': movie_detail_list}

    return render(request, 'movie-list-template.html', {'final_dict': final_dict, 'title': title})


@get_time
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@renderer_classes([TemplateHTMLRenderer])
def get_movie_detail(request, imdb_id):
    f = open('movies_info.dat')
    movie_dataset = eval(f.read())
    f.close()

    movie_list = movie_dataset.get('movie_list')
    movie_list = list(filter(lambda x: imdb_id in x.get('imdbID').lower(), movie_list))
    if len(movie_list):
        final_dict = movie_list[0]
    print (list(movie_list))
    
    return render(request, 'movie-detail-template.html', {'final_dict': final_dict})
