from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    from .models import NewsHeadlines
    headlines = NewsHeadlines.objects.all()
    context = {'headlines': headlines, }

    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'infoweb/index.html', context)
