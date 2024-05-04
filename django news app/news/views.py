from django.shortcuts import render
from django.http import JsonResponse
import json


def home(request):
    import requests
    import json
    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=7be263f74726464ba9a86a4496a7f21f")
    api=json.loads(news_api_request.content)
    return render(request,'index.html',{'api':api})
