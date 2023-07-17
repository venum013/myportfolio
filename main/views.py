from django.shortcuts import render
from .models import CV

# Create your views here.
def index(request):
    cv = CV.objects.all()[0]
 
    return render(request=request,template_name='main/index.html',context={'cv' : cv},)