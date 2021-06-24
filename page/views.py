from .models import Team
from django.shortcuts import render

# Create your views here.
def home(request):
    Teams= Team.objects.all()
    context={
          'Teams':Teams,
        }   
    return render(request,'home.html',context)