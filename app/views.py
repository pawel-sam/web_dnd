import json
from django.shortcuts import render


def index(request):
    with open('map.json') as f:
        data = json.load(f)
    return render(request, 'index.html', {"datad": data})
