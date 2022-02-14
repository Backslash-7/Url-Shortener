from django.shortcuts import redirect, render
from django.http import HttpResponse
from Url_App.models import Url

# Create your views here.
def home(request):
    if request.method == "POST":
        Your_url = request.POST.get('Your_url')
        obj = Url.create(Your_url)
        return render(request, 'index.html', {
            'Your_url' : obj.Your_url,
            'short_url' : request.get_host() + '/' + obj.short_url
        })
    
    return render(request, 'index.html')

def home_url(request, key):
    try:
        obj = Url.objects.get(short_url=key)
        return redirect(obj.Your_url)
    except:
        return redirect(home)

