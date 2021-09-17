from django.shortcuts import render
from.models import Treasure

def index(request):
    return render(request, 'index.html')
    
def map(request):
    treasures = Treasure.objects.filter(placed_by=request.user)
    context = {'treasures':treasures}
    return render(request, 'map.html', context)

def profile(request):
    if request.method == 'GET': 
        treasures = Treasure.objects.filter(placed_by=request.user)
        context = {'treasures':treasures}
        return render(request, 'profile.html', context)
    if request.method == 'POST':
        lat = request.POST['lat']
        long = request.POST['long']
        comments = request.POST['comments']
        user = request.user
        Treasure.objects.create(x_coordinate=lat, y_coordinate=long, notes=comments, placed_by=user, new=True)
        treasures = Treasure.objects.filter(placed_by=request.user)
        context = {'treasures':treasures}
        return render(request, 'profile.html', context)