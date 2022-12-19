from django.shortcuts import render

# Create your views here.


def index(request, *args, **kwargs):
    # chat/ html file name
    context = {}
    return render(request, 'index.html', context)
