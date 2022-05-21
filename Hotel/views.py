from django.shortcuts import render

import requests

# Create your views here.
def index(request):
    # print(dir(request))

    # url = "http://img.omdbapi.com/?apikey=a93098f1"
    
    search = request.POST['search']
    # print(search, 'nnnnnnnnnnnnnnnnnnn')
    url = f"http://www.omdbapi.com/?t={search}&apikey=a93098f1"
    # params = {
    #     "t": "The Matrix"}
    response = requests.get(url)#, params=params)
    print(response.json())
    
    return render(request, 'index.html', { 'Data' : response.json()})



