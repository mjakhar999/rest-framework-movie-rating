from rest_framework.response import Response
from rest_framework import status
from watchlist.models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializers = MovieSerializer(movies,many=True) #many for querysets 
        return Response(serializers.data)
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        print(request.get['name'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','PUT','DELETE'])
def movie_byid(request,pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({"Error":"movie not found"},status =404)
    if request.method =='GET':
        movies = Movie.objects.get(pk=pk)
        serializers = MovieSerializer(movies)
        return Response(serializers.data)
    
    if request.method == 'PUT':
        movies = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 

    if request.method == 'DELETE':
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
        except Movie.DoesNotExist:
            return Response({"Error":"movie not found"},status =404)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
