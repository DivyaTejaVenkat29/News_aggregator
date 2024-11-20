from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

# Load data once when the app starts
df = pd.read_csv("D:\\News Aggregator\\Categorization\\news_articles.csv")

# View to render the HTML template
def articles_search(request):
    return render(request, 'articles.html')

# View to get all articles
@api_view(['GET'])
def get_articles(request):
    articles = df.to_dict(orient='records')
    return Response(articles)

# View to get an article by ID
@api_view(['GET'])
def get_article(request, id):
    if id >= len(df) or id < 0:
        return Response({"detail": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response(df.iloc[id].to_dict())

# View to search articles by query
@api_view(['GET'])
def search_articles(request):
    query = request.query_params.get('query', None)
    if query:
        search_results = df[
            df['Title'].str.contains(query, case=False, na=False) |
            df['Summary'].str.contains(query, case=False, na=False)
        ]
        if search_results.empty:
            return Response({"detail": "No articles found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(search_results.to_dict(orient='records'))
    return Response({"detail": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
