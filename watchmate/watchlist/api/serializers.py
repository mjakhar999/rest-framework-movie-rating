from rest_framework import serializers
from watchlist.models import Movie
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self,validate_data):
        return Movie.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.name = validate_data.get('name',instance)
        instance.description = validate_data.get('description',instance)
        instance.active = validate_data.get('active',instance)
        instance.save()
        return instance

