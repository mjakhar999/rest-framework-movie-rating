# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse,HttpResponse
# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     print(movies.values())
#     return JsonResponse({'movie':list(movies.values())})

# def movie(request,num):
#     m = Movie.objects.get(pk=num)
#     # return JsonResponse({'movie':m})
#     return HttpResponse(m.name)