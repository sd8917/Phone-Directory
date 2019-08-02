from django.shortcuts import render

from .models import Phone


# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')

        p = Phone(name=name, number=number)
        p.save()

        return render(request, 'phone/index.html', {'message': 'Your phone number is added'})

    else:
        return render(request, 'phone/index.html')


def show(request):
    names = Phone.objects.all()

    return render(request, 'phone/show.html', {'names': names})
