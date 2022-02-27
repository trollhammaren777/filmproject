from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import Movie, Director, Genre


@registry.register_document
class MovieDocument(Document):
    class Index:
        name = "movies"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Movie
        fields = [
            "title",
            "release_date",
            "price",
        ]


@registry.register_document
class DirectorDocument(Document):
    class Index:
        name = "directors"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Director
        fields = [
            "full_name",
            "birth_date",
            "age",
        ]


@registry.register_document
class GenreDocument(Document):
    class Index:
        name = "genres"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Genre
        fields = [
            "name",
        ]
