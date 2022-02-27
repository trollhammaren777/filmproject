from rest_framework.serializers import ModelSerializer

from .models import Director, Movie, Genre


class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
