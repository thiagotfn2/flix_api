from django.db.models import Avg
from rest_framework import serializers
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'    

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1950.')
        return value
        
    def validate_resume(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError('O resumo não seve ser maior do que 1000 caracteres.')
        return value

class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
                        
        return None