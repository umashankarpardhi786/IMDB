from django.shortcuts import render
from IMDB.settings import IMDB_FILE
import json

def showIndex(request):
    json.loads(open(IMDB_FILE).read())
    return render(request,"index.html")