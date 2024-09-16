from django.shortcuts import render
import requests  
import urllib.request 
import json
API_KEY = 'dfa5d1a88fdc4465aca2a49e58f116bb'



def home(request):
    if request.method=='POST':
        city = request.POST['city']
    else:
        city = ''
        
    
    return render(request, 'home.html', {"city":city})


def index(request):
    if request.method=='POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=bdcfa98d22f4568dd28cc0e7b39873da').read()
        data1 = json.loads(res)
        data = {
            "Country_Code": str(data1['sys']['country']),
            "Coordinate": str(data1['coord']['lon'])  + ' ' + str(data1['coord']['lat']),
            "Temperature":str(data1['main']['temp'])+'k',
            "Pressure": str(data1['main']['pressure']),
            "Humidity": str(data1['main']['humidity'] ),
        }
    else:
        city = ''
        data  = ''
    
    return render(request, 'home.html', {"city":city, "data":data})

def news(request):
    country = request.GET.get('country')
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    response = requests.get(url)
    json_data = response.json()
    articles = json_data['articles']
    

    
    
    return render(request, 'news.html', {"articles":articles})
    