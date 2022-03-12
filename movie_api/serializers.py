from dataclasses import field
from rest_framework import serializers
from movie_api.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
