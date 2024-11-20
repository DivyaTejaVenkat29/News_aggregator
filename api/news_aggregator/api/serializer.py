from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    Title = serializers.CharField(max_length=200)
    Summary = serializers.CharField()
    Publication_Date = serializers.DateTimeField()
    Source = serializers.CharField(max_length=100)
    URL = serializers.URLField()
    Category = serializers.CharField(max_length=100)
