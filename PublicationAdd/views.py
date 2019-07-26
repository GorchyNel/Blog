from django.shortcuts import render

def add_publication(request):
    return render(request, 'add_publication.html', locals())
