from django.shortcuts import render
from .models import *
# Create your views here.
def index(malumot):
    malumotlaz = Portfolio.objects.all()
    malumotlar = Team.objects.all()
    malumotla = Services.objects.all()
    return render(malumot,'index.html',{"Portfolio":malumotlaz,"Team":malumotlar,"service":malumotla})

def portfolio(malumot,id):
    data = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{"port":data})

def adminga_murojaat(malumot):
    if malumot.method == 'POST':
        name = malumot.POST.get("name")
        email = malumot.POST.get("email")
        subject = malumot.POST.get("subject")
        message = malumot.POST.get("message")

        Adminga_murojaat(name=name,email=email,message=message,subject=subject).save()
    return render(malumot,'index.html')


